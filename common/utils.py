import uuid

from adminsortable2.admin import SortableAdminMixin
from django.contrib import messages

# noinspection PyProtectedMember
from django.contrib.admin import ModelAdmin

IMAGE_WITH_PREVIEW = ('image', 'image_thumbnail')
NAME_SLUG = ('name', 'slug')
CREATED_UPDATED = ('Created/Updated', {'classes': ('collapse',), 'fields': (('created', 'updated',),)})


def get_upload_path(instance, file_name):
    """
    Takes filename and creates new one with random string at the end
    :param instance: DO NOT delete this parameter, it's required for upload_to
    :param file_name: raw file name from admin
    :return: new file name
    """
    if instance.offer is None:
        file_name, extension = file_name.split('.')
        return f'{file_name}_{str(uuid.uuid4())[:8]}.{extension}'

    model = instance.offer.__class__._meta
    model_name = model.verbose_name_plural.replace(' ', '_')
    file_name, extension = file_name.split('.')
    file_path = f'{model_name}/{file_name}_{str(uuid.uuid4())[:8]}.{extension}'
    return file_path


def message_info(request, message):
    messages.add_message(request, messages.INFO, message)


def message_error(request, message):
    messages.add_message(request, messages.ERROR, message)


# this function is meant to override default get_max_order if object is newly created
# noinspection PyUnusedLocal
def get_max_order(request, obj, *args, **kwargs):
    return 0


class SortableModelAdmin(SortableAdminMixin, ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            for item in self.model.objects.all():
                item.order_index += 1
                item.save()
            SortableAdminMixin.get_max_order = get_max_order
        super().save_model(request, obj, form, change)


class PrepopulatedSlugAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

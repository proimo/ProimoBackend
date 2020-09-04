import admin_thumbnails
from django.contrib.admin import TabularInline, ModelAdmin
from django.db import models

from administration.models import UserProfile
from main.models import BaseModel
from main.utils import get_upload_path


def remove_agent_field_from(fieldsets):
    for fieldset in fieldsets:
        fieldset[1]['fields'] = [field for field in fieldset[1]['fields'] if not field.__eq__('agent')]

    return fieldsets


#######################################
# Base classes both for models and admin
class BaseOfferModel(BaseModel):
    agent = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.CharField(max_length=500, default=None, null=True)
    is_published = models.BooleanField('publicat?', default=False)

    class Meta:
        abstract = True


class BaseOfferAdmin(ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug', 'agent',)})
    time_fieldsets = ('Creat/Modificat', {
        'classes': ('collapse',),
        'fields': ('created', 'updated',)
    })

    list_display_links = ['name']
    prepopulated_fields = {'slug': ['name', ]}

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(BaseOfferAdmin, self).get_fieldsets(request, obj)
        if request.user.is_superuser is not True:
            fieldsets = remove_agent_field_from(fieldsets)
        return fieldsets

    def save_model(self, request, obj, form, change):
        if obj.agent is None:
            obj.agent = UserProfile.objects.get(user=request.user)
        super(BaseOfferAdmin, self).save_model(request, obj, form, change)

    class Meta:
        abstract = True


class OfferImages(models.Model):
    image = models.ImageField('imagine', upload_to=get_upload_path, blank=True, default=None)

    def __str__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = 'imagine'
        verbose_name_plural = 'imagini'


@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(TabularInline):
    extra = 0

    class Meta:
        abstract = True

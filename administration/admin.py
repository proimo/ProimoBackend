from typing import Tuple

import admin_thumbnails
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin, site, TabularInline, EmptyFieldListFilter, SimpleListFilter
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin, Group as BaseGroup
from django.db.models import QuerySet, Q
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from administration.models import User, UserProfile, Group, Setting, MenuItem
from common.utils import SortableModelAdmin, NAME_SLUG, IMAGE_WITH_PREVIEW, CREATED_UPDATED, PrepopulatedSlugAdmin


def remove_user_model(app):
    for model in app['models']:
        if model['object_name'].__eq__('User'):
            app['models'].remove(model)


def should_collapse(fieldset: Tuple) -> bool:
    has_big_widgets = fieldset[0].__eq__(_('Important dates')) or fieldset[0].__eq__(_('Permissions'))
    return has_big_widgets and fieldset[0] is not None


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    if request.user.is_active and request.user.is_superuser:
        return app_list

    # If it's not superuser, remove 'User' model from de model list
    for app in app_list:
        if app['app_label'].__eq__('administration'):
            remove_user_model(app)
            if not app['models']:
                app_list.remove(app)

    return app_list


admin.AdminSite.get_app_list = get_app_list


@admin.register(Setting)
class SettingAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'value', 'image')
    search_fields = ['name', 'slug', 'value']
    prepopulated_fields = {'slug': ('name',)}


class UserProfileInline(StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name')
    autocomplete_fields = ('user',)


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    search_fields = ('username', 'first_name', 'last_name')

    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            return redirect('/api/admin/')
        return super(UserAdmin, self).changelist_view(request, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.is_active and request.user.is_superuser:
            return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context)

        if not str(request.user.id).__eq__(object_id):
            return redirect('/api/admin/')
        return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_active and request.user.is_superuser:
            fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
            for fieldset in fieldsets:
                if should_collapse(fieldset):
                    fieldset[1]['classes'] = ('collapse',)
            return fieldsets

        return [(None, {'fields': ('username',)}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}), ]

    def response_change(self, request, obj):
        if request.user.is_active and request.user.is_superuser:
            return super(UserAdmin, self).response_change(request, obj)

        # Redirect user that is not superuser to index page
        return redirect('/api/admin/')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


site.unregister(BaseGroup)
site.register(Group, GroupAdmin)
site.register(User, UserAdmin)


class MenuItemsParentFilter(SimpleListFilter):
    title = 'parent'
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        queryset: QuerySet[MenuItem] = model_admin.get_queryset(request)
        return [(item.id, item.name) for item in queryset if not item.parent]

    def get_children_filter(self):
        filters = Q(pk=0)
        for item in MenuItem.objects.filter(parent__id=self.value()):
            if children_filter := item.get_children_filter(include_self=True):
                filters |= children_filter
        return filters

    def queryset(self, request, queryset: QuerySet[MenuItem]):
        if self.value():
            return queryset.filter(self.get_children_filter())


@admin_thumbnails.thumbnail('image', background=True)
class MenuItemInline(SortableInlineAdminMixin, TabularInline):
    model = MenuItem
    fields = ('name', 'slug', 'link', 'image', 'type', 'parent', 'is_published', 'is_long')
    extra = 0
    verbose_name = 'Child'
    verbose_name_plural = 'Children'


@admin.register(MenuItem)
@admin_thumbnails.thumbnail('image', background=True)
class MenuItemAdmin(SortableModelAdmin, PrepopulatedSlugAdmin):
    inlines = (MenuItemInline, )
    fieldsets = ((None, {'fields': (NAME_SLUG, 'link', 'description', IMAGE_WITH_PREVIEW, 'type', 'parent',
                                    ('is_published', 'is_long',),)}), CREATED_UPDATED)
    autocomplete_fields = ('parent',)
    search_fields = ('name',)

    list_display = ('name', 'slug', 'parent', 'type', 'is_published', 'image_thumbnail', 'order_index')
    list_editable = ('parent', 'is_published', 'type')
    list_filter = (MenuItemsParentFilter, ('parent', EmptyFieldListFilter), 'type')

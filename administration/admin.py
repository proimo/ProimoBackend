from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin, Group as BaseGroup
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from administration.models import User, UserProfile, Group, Setting


def remove_user_model(app):
    for model in app['models']:
        if model['object_name'].__eq__('User'):
            app['models'].remove(model)


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    if request.user.is_active and request.user.is_superuser:
        return app_list

    # If it's not superuser, remove 'User' model from de model list
    for app in app_list:
        if app['app_label'].__eq__('administration'):
            remove_user_model(app)
            if len(app['models']) == 0:
                app_list.remove(app)

    return app_list


admin.AdminSite.get_app_list = get_app_list


class SettingAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'value', 'image')
    search_fields = ['name', 'slug', 'value']
    prepopulated_fields = {'slug': ('name',)}


class UserProfileInline(StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

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
                if (fieldset[0].__eq__(_('Important dates')) or fieldset[0].__eq__(_('Permissions'))) and fieldset[0] is not None:
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
site.register(Setting, SettingAdmin)
site.register(User, UserAdmin)

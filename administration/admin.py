import re

from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin, Group as BaseGroup
from django.http import HttpResponseBadRequest

from administration.models import User, UserProfile, Group, Setting


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    if request.user.is_active and request.user.is_superuser:
        return app_list

    # Return all but 'Administration' app if it's not superuser
    return [j for i, j in enumerate(app_list) if not j['app_label'].__eq__('administration')]


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

    def get_fieldsets(self, request, obj=None):
        if request.user.is_active and request.user.is_superuser:
            return super(UserAdmin, self).get_fieldsets(request, obj)

        try:
            user_id = re.findall(r'user/(\d+)/change', str(request))[0]
        except IndexError:
            raise HttpResponseBadRequest("You ran into troubles, gangsta!")
        if not str(request.user.id).__eq__(user_id):
            raise HttpResponseBadRequest("You're not allowed to do that, bad boy!")

        return [(None, {'fields': ('username', 'password',)}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'email')}), ]


site.unregister(BaseGroup)
site.register(Group, GroupAdmin)
site.register(Setting, SettingAdmin)
site.register(User, UserAdmin)

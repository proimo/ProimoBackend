import json
import re
from pprint import pprint

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin, Group as BaseGroup
from django.http import HttpRequest
from django.shortcuts import redirect

import administration
from administration.forms import ProfileForm, EditProfileForm
from administration.models import User, UserProfile, Group, Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'value', 'image')
    search_fields = ['name', 'slug', 'value']
    prepopulated_fields = {'slug': ('name',)}

    # class Meta:
    #     app_label =


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     form = ProfileForm
#     list_display = ('phone_number', 'image')
#     change_form_template = 'admin/edit_profile.html'
#
#     def render_change_form(self, request, context, *args, **kwargs):
#         # extra = {'lame_static_text': "something static", }
#         # context.update(extra)
#         return super(UserProfileAdmin, self).render_change_form(request, context, *args, **kwargs)
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def get_form(self, request, *args, **kwargs):
        form = super(UserAdmin, self).get_form(request, *args, **kwargs)
        return form

    def get_fieldsets(self, request, obj=None):
        if request.user.is_active and request.user.is_superuser:
            fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
            print(fieldsets)
            return fieldsets

        user_id = re.findall(r'user/(\d+)/change', str(request))[0]
        if user_id is not str(request.user.id):
            redirect('/api/admin')
        print(user_id)
        return [(None, {'fields': ('username', 'password',)}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'email')}), ]


class PLM(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(BaseGroup)
admin.site.register(Group, GroupAdmin)

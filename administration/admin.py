from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin, Group as BaseGroup

from administration.models import User, UserProfile, Group, Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'value', 'image')
    search_fields = ['name', 'slug', 'value']
    prepopulated_fields = {'slug': ('name',)}


admin.site.unregister(BaseGroup)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

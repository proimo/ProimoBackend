from django.contrib import admin

# Register your models here.

from website.models import Announcement, AnnouncementImage, Setting


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']
    inlines = [AnnouncementImageInline]


class SettingAdmin(admin.ModelAdmin):
    list_display = ('slug', 'value', 'image')
    search_fields = ['slug', 'value']


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Setting, SettingAdmin)

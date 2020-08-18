from django.contrib import admin

# Register your models here.

from website.models import Announcement, AnnouncementImage, Setting


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']
    inlines = [AnnouncementImageInline]


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('slug', 'value', 'image')
    search_fields = ['slug', 'value']

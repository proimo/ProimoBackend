from django.contrib import admin

from website.models import Announcement, AnnouncementImage


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']
    inlines = [AnnouncementImageInline]

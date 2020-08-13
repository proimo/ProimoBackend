from django.contrib import admin

# Register your models here.

from website.models import Announcement, AnnouncementImage


class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']
    inlines = [AnnouncementImageInline]


admin.site.register(Announcement, AnnouncementAdmin)

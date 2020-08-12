from django.contrib import admin

# Register your models here.

from website.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']


admin.site.register(Announcement, AnnouncementAdmin)

from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from common.models import County, Locality

DEFAULT_PREPOPULATED_SLUG = {'slug': ['name', ]}
DEFAULT_SEARCH_FIELDS = ('name', 'slug')


class BaseModelAdmin(ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug')})
    time_fieldsets = ('Creat/Modificat', {'classes': ('collapse', 'wide'), 'fields': ('created', 'updated',)})
    prepopulated_fields = DEFAULT_PREPOPULATED_SLUG
    search_fields = DEFAULT_SEARCH_FIELDS
    date_hierarchy = 'created'
    list_display = ('name', 'slug')
    list_filter = ('created', 'updated')
    fieldsets = (basic_info_fieldsets, time_fieldsets)


@admin.register(Locality)
class LocalityAdmin(BaseModelAdmin):
    pass


class LocalityInline(TabularInline):
    model = Locality
    fields = ('name', 'slug')
    classes = ('collapse',)
    extra = 0


@admin.register(County)
class CountyAdmin(BaseModelAdmin):
    inlines = (LocalityInline,)

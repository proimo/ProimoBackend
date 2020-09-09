from django.contrib import admin
from django.contrib.admin import ModelAdmin

from common.models import County, Locality

DEFAULT_PREPOPULATED_SLUG = {'slug': ['name', ]}


class BaseModelAdmin(ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug')})
    time_fieldsets = ('Creat/Modificat', {'classes': ('collapse', 'wide'), 'fields': ('created', 'updated',)})
    prepopulated_fields = DEFAULT_PREPOPULATED_SLUG


@admin.register(County)
class CountyAdmin(BaseModelAdmin):
    pass


@admin.register(Locality)
class LocalityAdmin(BaseModelAdmin):
    pass

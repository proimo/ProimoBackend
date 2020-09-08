from django.contrib import admin

# Register your models here.
from common.models import County, Locality


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    pass


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    pass

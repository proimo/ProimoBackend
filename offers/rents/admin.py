from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.rents.models import ApartmentRent, HouseRent, LandRent, CommercialSpaceRent, OfficeRent, \
    SpecialPropertyRent, IndustrialSpaceRent


# class OfferImageInline(admin.TabularInline):
#     model = OfferImage
#     extra = 0


class RentOfferAdmin(admin.ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug')})
    other_fieldsets = (None, {'fields': ('price', 'content')})
    location_fieldsets = ('Localizare', {'fields': ('region', 'address')})
    time_fieldsets = ('Creat/Modificat', {
        'classes': ('collapse',),
        'fields': ('created', 'updated',)
    })

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        basic_info_fieldsets,
        location_fieldsets,
        other_fieldsets,
        time_fieldsets
    )
    list_display = ('name', 'slug', 'region', 'address', 'price')
    list_display_links = ['name']
    prepopulated_fields = {'slug': ['name', ]}
    list_filter = ['region', 'created', 'updated']
    search_fields = ['name', 'slug', 'address']


#     inlines = [OfferImageInline]


@admin.register(ApartmentRent)
class ApartmentRentAdmin(RentOfferAdmin):
    fieldsets = (
        RentOfferAdmin.basic_info_fieldsets,
        RentOfferAdmin.location_fieldsets,
        RentOfferAdmin.other_fieldsets,
        RentOfferAdmin.time_fieldsets
    )


@admin.register(HouseRent)
class HouseRentAdmin(RentOfferAdmin):
    pass


@admin.register(LandRent)
class LandRentAdmin(RentOfferAdmin):
    pass


@admin.register(CommercialSpaceRent)
class CommercialSpaceRentAdmin(RentOfferAdmin):
    pass


@admin.register(OfficeRent)
class OfficeRentAdmin(RentOfferAdmin):
    pass


@admin.register(SpecialPropertyRent)
class SpecialPropertyRentAdmin(RentOfferAdmin):
    pass


@admin.register(IndustrialSpaceRent)
class IndustrialSpaceRentAdmin(RentOfferAdmin):
    pass

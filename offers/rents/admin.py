from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.models import OfferImageInline
from offers.rents.models import ApartmentRent, HouseRent, LandRent, CommercialSpaceRent, OfficeRent, \
    SpecialPropertyRent, IndustrialSpaceRent, ApartmentRentImages, HouseRentImages, LandRentImages, \
    CommercialSpaceRentImages, OfficeRentImages, SpecialPropertyRentImages, IndustrialSpaceRentImages


#######################################
# Model's base admin inline / model
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


#######################################
# Model's inlines
class ApartmentRentImagesInline(OfferImageInline):
    model = ApartmentRentImages


class HouseRentImagesInline(OfferImageInline):
    model = HouseRentImages


class LandRentImagesInline(OfferImageInline):
    model = LandRentImages


class CommercialSpaceRentImagesInline(OfferImageInline):
    model = CommercialSpaceRentImages


class OfficeRentImagesInline(OfferImageInline):
    model = OfficeRentImages


class SpecialPropertyRentImagesInline(OfferImageInline):
    model = SpecialPropertyRentImages


class IndustrialSpaceRentImagesInline(OfferImageInline):
    model = IndustrialSpaceRentImages


#######################################
# Model's admin configs
@admin.register(ApartmentRent)
class ApartmentRentAdmin(RentOfferAdmin):
    inlines = (ApartmentRentImagesInline,)
    fieldsets = (
        RentOfferAdmin.basic_info_fieldsets,
        RentOfferAdmin.location_fieldsets,
        RentOfferAdmin.other_fieldsets,
        RentOfferAdmin.time_fieldsets
    )


@admin.register(HouseRent)
class HouseRentAdmin(RentOfferAdmin):
    inlines = (HouseRentImagesInline,)


@admin.register(LandRent)
class LandRentAdmin(RentOfferAdmin):
    inlines = (LandRentImagesInline,)


@admin.register(CommercialSpaceRent)
class CommercialSpaceRentAdmin(RentOfferAdmin):
    inlines = (CommercialSpaceRentImagesInline,)


@admin.register(OfficeRent)
class OfficeRentAdmin(RentOfferAdmin):
    inlines = (OfficeRentImagesInline,)


@admin.register(SpecialPropertyRent)
class SpecialPropertyRentAdmin(RentOfferAdmin):
    inlines = (SpecialPropertyRentImagesInline,)


@admin.register(IndustrialSpaceRent)
class IndustrialSpaceRentAdmin(RentOfferAdmin):
    inlines = (IndustrialSpaceRentImagesInline,)

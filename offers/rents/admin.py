from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.models import OfferImageInline, BaseOfferAdmin
from offers.rents.models import ApartmentRent, HouseRent, LandRent, CommercialSpaceRent, OfficeRent, \
    SpecialPropertyRent, IndustrialSpaceRent, ApartmentRentImages, HouseRentImages, LandRentImages, \
    CommercialSpaceRentImages, OfficeRentImages, SpecialPropertyRentImages, IndustrialSpaceRentImages


#######################################
# Model's base admin inline / model
class RentOfferAdmin(BaseOfferAdmin):
    other_fieldsets = (None, {'fields': ('content',)})

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        other_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )
    list_display = ('name', 'slug', 'address')
    list_filter = ['created', 'updated']
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
    rent_fieldset = ('Chirie', {'fields': (('rent_cost', 'rent_currency'), 'zero_commission', 'buyer_commission')})
    characteristics_fieldset = ('Caracteristici principale', {'fields': (
        'rooms_nr', 'util_surface', 'constructed_surface', 'level', 'levels_nr', 'building_type', 'bathrooms_nr',
        'partitioning_type', 'comfort')})
    other_details_fieldset = ('Detalii suplimentare', {'fields': ('other_details',)})
    fieldsets = (
        RentOfferAdmin.basic_info_fieldsets,
        RentOfferAdmin.location_fieldsets,
        rent_fieldset,
        characteristics_fieldset,
        other_details_fieldset,
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

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from offers.admin import BaseOfferAdmin, OfferImageInline, HouseBaseAdmin, LandBaseAdmin
from offers.fieldsets import rent_price_fieldsets, property_info_fieldsets, exclusivity_fieldsets
from offers.rents.models import ApartmentRent, HouseRent, LandRent, CommercialSpaceRent, OfficeRent, \
    SpecialPropertyRent, IndustrialSpaceRent, ApartmentRentImages, HouseRentImages, LandRentImages, \
    CommercialSpaceRentImages, OfficeRentImages, SpecialPropertyRentImages, IndustrialSpaceRentImages, SpaceModel


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


class SpaceInline(GenericStackedInline):
    model = SpaceModel
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'name', 'surface', ('disponibility', 'disponibility_time'), ('rent_cost', 'rent_currency'),
                ('hide_price', 'not_include_vat', 'has_maintenance', 'zero_commission'), 'rent_commission', 'level',
                'divisible_space', 'description', 'has_parking')}),
    )


#######################################
# Model's admin configs
@admin.register(ApartmentRent)
class ApartmentRentAdmin(BaseOfferAdmin):
    inlines = (ApartmentRentImagesInline,)
    rent_fieldset = (
        'Chirie', {
            'fields': (('rent_cost', 'rent_currency'), 'zero_commission', 'buyer_commission')})
    characteristics_fieldset = (
        'Caracteristici principale', {
            'fields': ('rooms_nr', 'util_surface', 'constructed_surface', 'level', 'levels_nr', 'building_type',
                       'bathrooms_nr', 'partitioning_type', 'comfort')})
    other_details_fieldset = (
        'Detalii suplimentare', {
            'fields': ('other_details',)})

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        rent_fieldset,
        characteristics_fieldset,
        other_details_fieldset,
        BaseOfferAdmin.time_fieldsets
    )


@admin.register(HouseRent)
class HouseRentAdmin(HouseBaseAdmin):
    inlines = (HouseRentImagesInline,)
    fieldsets = HouseBaseAdmin.fieldsets[:2] + (rent_price_fieldsets,) + HouseBaseAdmin.fieldsets[2:]


@admin.register(LandRent)
class LandSaleAdmin(LandBaseAdmin):
    inlines = (LandRentImagesInline,)
    fieldsets = LandBaseAdmin.fieldsets[:2] + (rent_price_fieldsets,) + LandBaseAdmin.fieldsets[2:]


@admin.register(CommercialSpaceRent)
class CommercialSpaceRentAdmin(BaseOfferAdmin):
    inlines = (CommercialSpaceRentImagesInline,)


@admin.register(OfficeRent)
class OfficeRentAdmin(BaseOfferAdmin):
    inlines = (SpaceInline, OfficeRentImagesInline)

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        ('Tip spaţiu', {
            'fields': ('building_type',)}),
        property_info_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(SpecialPropertyRent)
class SpecialPropertyRentAdmin(BaseOfferAdmin):
    inlines = (SpecialPropertyRentImagesInline,)


@admin.register(IndustrialSpaceRent)
class IndustrialSpaceRentAdmin(BaseOfferAdmin):
    inlines = (IndustrialSpaceRentImagesInline,)

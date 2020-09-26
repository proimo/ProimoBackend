from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from offers.admin import BaseOfferAdmin, OfferImageInline, HouseBaseAdmin, LandBaseAdmin
from offers.fieldsets import rent_price_fieldsets, exclusivity_fieldsets, get_property_info_fieldsets, \
    default_property_info_fields, get_additional_property_info_fieldsets, space_utilities_fields, \
    default_additional_property_info_fields
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
                'name', 'surface',
                ('disponibility', 'disponibility_time'),
                ('rent_cost', 'rent_currency', 'hide_price'),
                ('not_include_vat', 'has_maintenance', 'zero_commission'),
                'rent_commission', 'space_height', 'has_show_window')}),
        ('Câmpuri suplimentare', {
            'fields': ('level', 'divisible_space', 'description', 'has_parking'),
            'classes': ('collapse',)
        })
    )


class IndustrialSpaceInline(GenericStackedInline):
    model = SpaceModel
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'name', 'surface',
                ('disponibility', 'disponibility_time'),
                ('rent_cost', 'rent_currency', 'hide_price'),
                ('not_include_vat', 'has_maintenance', 'zero_commission'),
                'rent_commission', 'space_height')}),
        ('Câmpuri suplimentare', {
            'fields': ('divisible_space', 'flooring_type', 'description', 'previous_purpose', 'offices_surface',
                       ('has_heating_system', 'has_air_conditioning', 'has_windows', 'has_lighting')),
            'classes': ('collapse',)
        })
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
    inlines = (SpaceInline, CommercialSpaceRentImagesInline,)
    commercial_property_fields = default_property_info_fields[:3] + default_property_info_fields[4:]
    additional_property_info_fieldsets = default_additional_property_info_fields + space_utilities_fields

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        ('Tip spaţiu', {
            'fields': ('building_type',)}),
        get_property_info_fieldsets(commercial_property_fields),
        get_additional_property_info_fieldsets(collapsed=True, fields=additional_property_info_fieldsets),
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(OfficeRent)
class OfficeRentAdmin(BaseOfferAdmin):
    inlines = (SpaceInline, OfficeRentImagesInline)

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        ('Tip spaţiu', {
            'fields': ('building_type',)}),
        get_property_info_fieldsets(),
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(SpecialPropertyRent)
class SpecialPropertyRentAdmin(BaseOfferAdmin):
    inlines = (SpaceInline, SpecialPropertyRentImagesInline)
    commercial_property_fields = default_property_info_fields[:3] + default_property_info_fields[4:]
    additional_property_info_fieldsets = default_additional_property_info_fields + space_utilities_fields

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        ('Tip spaţiu', {
            'fields': ('building_type',)}),
        get_property_info_fieldsets(commercial_property_fields),
        get_additional_property_info_fieldsets(collapsed=True, fields=additional_property_info_fieldsets),
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(IndustrialSpaceRent)
class IndustrialSpaceRentAdmin(BaseOfferAdmin):
    inlines = (IndustrialSpaceInline, IndustrialSpaceRentImagesInline)
    property_fields = default_property_info_fields[:3] + default_property_info_fields[4:]
    additional_property_info_fieldsets = ('building_year', 'building_stage', 'occupation_degree', 'levels_nr',
                                          'resistance_structure', 'platform_surface')

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        ('Tip spaţiu', {
            'fields': ('building_type',)}),
        get_property_info_fieldsets(property_fields),
        get_additional_property_info_fieldsets(fields=additional_property_info_fieldsets),
        ('Utilităţi', {
            'fields': (('has_water', 'has_gas', 'has_current'),)
        }),
        ('Acces', {
            'fields': (('has_railway', 'has_tir_access', 'has_roads'),)
        }),
        ('Dotări', {
            'fields': (('has_ramp', 'has_slide_bridge', 'has_elevator', 'has_crane'),)
        }),
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )

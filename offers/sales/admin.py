from django.contrib import admin

from offers.admin import BaseOfferAdmin, OfferImageInline, HouseBaseAdmin, LandBaseAdmin
from offers.fieldsets import sale_price_fieldsets, rooms_fieldsets, other_fieldsets, destination_fieldsets, \
    exclusivity_fieldsets, space_price_fieldsets, space_type_fieldsets, space_utilities_fieldsets, \
    get_additional_property_info_fieldsets, other_zone_details_fieldsets, hotel_services_fieldsets, building_services_fieldsets, \
    building_features_fieldsets, diverse_fieldsets, appliances_fieldsets, furnished_fieldsets, counters_fieldsets, \
    kitchen_fieldsets, walls_fieldsets, interior_doors_fieldsets, floor_fieldsets, heat_isolation_fieldsets, \
    entrance_door_fieldsets, rolls_fieldsets, louver_fieldsets, windows_fieldsets, interior_state_fieldsets, \
    internet_fieldsets, climate_fieldsets, heating_system_fieldsets, get_property_info_fieldsets
from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale, ApartmentSaleImages, HouseSaleImages, LandSaleImages, \
    CommercialSpaceSaleImages, SpecialPropertySaleImages, IndustrialSpaceSaleImages, OfficeSaleImages


#######################################
# Model's inlines
class ApartmentSaleImagesInline(OfferImageInline):
    model = ApartmentSaleImages


class HouseSaleImagesInline(OfferImageInline):
    model = HouseSaleImages


class LandSaleImagesInline(OfferImageInline):
    model = LandSaleImages


class CommercialSpaceSaleImagesInline(OfferImageInline):
    model = CommercialSpaceSaleImages


class OfficeSaleImagesInline(OfferImageInline):
    model = OfficeSaleImages


class SpecialPropertySaleImagesInline(OfferImageInline):
    model = SpecialPropertySaleImages


class IndustrialSpaceSaleImagesInline(OfferImageInline):
    model = IndustrialSpaceSaleImages


#######################################
# Model's admin configs
@admin.register(ApartmentSale)
class ApartmentSaleAdmin(BaseOfferAdmin):
    inlines = (ApartmentSaleImagesInline,)
    apartment_characteristics_fieldsets = (
        'Caracteristici apartament', {
            'fields': ('apartment_type', 'partitioning_type', 'level', 'comfort', 'util_surface', 'total_util_surface',
                       'constructed_surface')})
    building_fieldsets = (
        'Imobil', {
            'fields': ('building_type', ('has_basement', 'has_semi_basement', 'has_ground_floor', 'levels_nr',
                                         'has_mansard'), 'building_year', 'building_period', 'resistance_structure')})
    general_utilities_fieldsets = (
        'Utilităţi generale', {
            'fields': (('has_current', 'has_water', 'has_sewerage'),
                       ('has_gas', 'has_catv', 'has_phone', 'has_international_phone'))})
    other_util_spaces_fieldsets = (
        'Alte spaţii utile', {
            'fields': (('has_terrace', 'has_service_wc', 'has_basement_box', 'has_storage_closet'),)})

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        sale_price_fieldsets,
        apartment_characteristics_fieldsets,
        rooms_fieldsets,
        building_fieldsets,
        other_fieldsets,
        destination_fieldsets,
        exclusivity_fieldsets,
        other_zone_details_fieldsets,
        general_utilities_fieldsets,
        heating_system_fieldsets,
        climate_fieldsets,
        internet_fieldsets,
        interior_state_fieldsets,
        windows_fieldsets,
        louver_fieldsets,
        rolls_fieldsets,
        entrance_door_fieldsets,
        heat_isolation_fieldsets,
        floor_fieldsets,
        interior_doors_fieldsets,
        walls_fieldsets,
        other_util_spaces_fieldsets,
        kitchen_fieldsets,
        counters_fieldsets,
        furnished_fieldsets,
        appliances_fieldsets,
        diverse_fieldsets,
        building_features_fieldsets,
        building_services_fieldsets,
        hotel_services_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )


@admin.register(HouseSale)
class HouseSaleAdmin(HouseBaseAdmin):
    inlines = (HouseSaleImagesInline,)
    fieldsets = HouseBaseAdmin.fieldsets[:2] + (sale_price_fieldsets,) + HouseBaseAdmin.fieldsets[2:]


@admin.register(LandSale)
class LandSaleAdmin(LandBaseAdmin):
    inlines = (LandSaleImagesInline,)
    fieldsets = LandBaseAdmin.fieldsets[:2] + (sale_price_fieldsets,) + LandBaseAdmin.fieldsets[2:]


@admin.register(CommercialSpaceSale)
class CommercialSpaceSaleAdmin(BaseOfferAdmin):
    inlines = (CommercialSpaceSaleImagesInline,)
    property_info_fieldsets = (
        'Informaţii proprietate', {
            'fields': ('property_name', 'property_description', 'total_surface', 'terrain_surface', 'space_height',
                       'has_show_window')})

    readonly_fields = ['has_ground_floor']
    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        get_additional_property_info_fieldsets(collapsed=True),
        space_utilities_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(OfficeSale)
class OfficeSaleAdmin(BaseOfferAdmin):
    inlines = (OfficeSaleImagesInline,)
    readonly_fields = ['has_ground_floor']
    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        get_property_info_fieldsets(),
        other_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(SpecialPropertySale)
class SpecialPropertySaleAdmin(BaseOfferAdmin):
    inlines = (SpecialPropertySaleImagesInline,)
    property_info_fieldsets = (
        'Informaţii proprietate', {
            'fields': ('property_name', 'property_description', 'total_surface', 'terrain_surface', 'space_height')})

    readonly_fields = ['has_ground_floor']
    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        get_additional_property_info_fieldsets(collapsed=True),
        space_utilities_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )


@admin.register(IndustrialSpaceSale)
class IndustrialSpaceSaleAdmin(BaseOfferAdmin):
    inlines = (IndustrialSpaceSaleImagesInline,)
    property_info_fieldsets = (
        'Informaţii proprietate', {
            'fields': ('property_name', 'property_description', 'total_surface', 'terrain_surface', 'space_height')})
    space_other_fieldsets = (
        'Câmpuri suplimentare', {
            'fields': ('building_year', 'building_stage', 'occupation_degree', 'levels_nr', 'min_divisible_surface',
                       'previous_purpose', 'offices_surface', 'flooring_type', 'resistance_structure',
                       'platform_surface')})
    utility_fieldsets = (
        'Utilităţi', {
            'fields': (('has_water', 'has_gas', 'has_current'),)})
    access_fieldsets = (
        'Acces', {
            'fields': (('has_railway', 'has_tir_access', 'has_roads'),)})
    features_fieldsets = (
        'Dotări', {
            'fields': (('has_ramp', 'has_slide_bridge', 'has_elevator', 'has_crane', 'has_heating_installation',
                        'has_air_conditioning', 'has_windows', 'has_lighting'),)})

    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        space_other_fieldsets,
        utility_fieldsets,
        access_fieldsets,
        features_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        BaseOfferAdmin.is_published_fieldsets
    )

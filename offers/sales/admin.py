from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.admin import BaseOfferAdmin, OfferImageInline
from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale, ApartmentSaleImages, HouseSaleImages, LandSaleImages, \
    CommercialSpaceSaleImages, SpecialPropertySaleImages, IndustrialSpaceSaleImages, OfficeSaleImages


#######################################
# Model's base admin inline / model
class SaleOfferAdmin(BaseOfferAdmin):
    other_fieldsets = (None, {'fields': ('is_published',)})
    location_fieldsets = ('Localizare', {'fields': ('county', 'locality', 'address',)})
    price_fieldsets = ('Preţ', {'fields': (
        'not_include_vat', 'price_details', 'zero_commission', 'buyer_commission'
    )})

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        location_fieldsets,
        price_fieldsets,
        other_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )

    list_display = ('name', 'slug', 'address')
    list_filter = ['created', 'updated']
    search_fields = ['name', 'slug', 'address']

    class Meta:
        abstract = True


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


price_fieldsets = ('Preţ', {'fields': (
    ('total_price', 'total_price_currency'), ('util_price', 'util_price_currency'),
    'not_include_vat', 'price_details', 'zero_commission', 'buyer_commission'
)})
space_price_fieldsets = ('Preţ', {
    'fields': (('price', 'price_currency'), 'hide_price', 'not_include_vat', 'price_details', 'zero_commission',
               'buyer_commission'
               )})
rooms_fieldsets = ('Încăperi şi anexe', {'fields': (('rooms_nr', 'garages_nr'), ('kitchens_nr', 'parking_lots_nr'),
                                                    ('balconies_nr', 'closed_balconies_nr'), 'bathrooms_nr')})
other_fieldsets = ('Alte detalii', {'fields': ('other_details', 'vices', 'display_expiry_date', 'disponibility')})
destination_fieldsets = ('Destinaţie', {'fields': (('is_residential', 'is_comercial', 'for_offices', 'for_vacation'),)})
exclusivity_fieldsets = ('Exclusivitate',
                         {'fields': ('has_exclusivity', 'contract', 'validity_from', 'validity_up_to'),
                          'classes': ('collapse',)})
other_zone_details_fieldsets = ('Alte detalii zonă', {
    'fields': (('asphalted_street', 'concreted_street', 'paved_street', 'soil_street', 'undeveloped_street'),
               ('has_illuminated_street', 'public_transport'))})
heating_system_fieldsets = ('Sistem încălzire', {'fields': (
    ('has_heating', 'has_own_boiler', 'has_building_boiler'),
    ('has_fireplace_or_terracotta', 'has_radiator', 'has_flooring_heating'))})
climate_fieldsets = ('Climatizare', {'fields': (('has_air_conditioning', 'has_fan', 'has_air_heater'),)})
internet_fieldsets = (
    'Acces internet', {'fields': (('has_wired_net', 'has_fiber', 'has_wireless', 'has_dial_up'),)})
interior_state_fieldsets = ('Stare interior', {'fields': (('is_renovated', 'is_good', 'need_renovation'),)})
windows_fieldsets = (
    'Ferestre cu geam termopan', {'fields': (('has_aluminium_windows', 'has_wood_windows', 'has_pvc_windows'),)})
louver_fieldsets = ('Jaluzele', {'fields': (('has_horizontal_louver', 'has_vertical_louver'),)})
rolls_fieldsets = ('Rulouri / obloane', {'fields': (('has_pvc_rolls', 'has_wood_rolls', 'has_aluminium_rolls'),)})
entrance_door_fieldsets = ('Uşă intrare', {'fields': (('has_pal_entrance_door', 'has_wood_entrance_door',
                                                       'has_metal_entrance_door', 'has_pvc_entrance_door',
                                                       'has_parquet_entrance_door'),)})
heat_isolation_fieldsets = (
    'Izolaţii termice', {'fields': (('has_indoor_heat_isolation', 'has_outdoor_heat_isolation'),)})
floor_fieldsets = ('Podele', {'fields': (('has_linoleum_floor', 'has_carpet_floor', 'has_parquet_floor',
                                          'has_tiles_floor', 'has_decking_floor', 'has_marble_floor'),)})
interior_doors_fieldsets = ('Uşi interior', {'fields': (('has_cellular_interior_door', 'has_wood_interior_door',
                                                         'has_panel_interior_door', 'has_pvc_interior_door',
                                                         'has_glass_interior_door'),)})
walls_fieldsets = ('Pereţi', {'fields': (('has_chalk_walls', 'has_vinarom_walls', 'has_washable_paint_walls',
                                          'has_faience_walls', 'has_wainscot_walls', 'has_wallpaper_walls',
                                          'has_clay_walls'),)})
kitchen_fieldsets = ('Bucătărie', {'fields': (
    ('has_furnished_kitchen', 'has_half_furnished_kitchen', 'has_equipped_kitchen', 'has_half_equipped_kitchen'),)})
counters_fieldsets = ('Contorizare', {'fields': (('has_gas_counter', 'has_water_counter', 'has_heat_counter'),)})
furnished_fieldsets = (
    'Mobilat', {'fields': (('is_not_furnished', 'is_half_furnished', 'is_full_furnished', 'is_lux_furnished'),)})
appliances_fieldsets = ('Electrocasnice', {'fields': (('has_iron', 'has_dishwasher', 'has_coffee_maker',
                                                       'has_wash_machine', 'has_toaster', 'has_fridge', 'has_oven',
                                                       'has_gas_cooker', 'has_hood', 'has_kitchen_robot',
                                                       'has_hairdryer', 'has_sandwich_maker', 'has_hi_fi', 'has_tv',
                                                       'has_vacuum_cleaner', 'has_dvd'),)})
diverse_fieldsets = ('Diverse', {'fields': (('has_smoke_sensor', 'has_alarm_system', 'has_fireplace',
                                             'has_jacuzzi',
                                             'has_garage_remote', 'has_auto_access_remote',
                                             'has_interior_stairway'),)})
building_features_fieldsets = ('Dotări imobil', {'fields': (('has_recreation_spaces', 'has_video_intercom',
                                                             'has_interior_pool', 'has_sauna', 'has_roof',
                                                             'has_yard', 'has_common_yard', 'has_garden',
                                                             'has_intercom', 'has_elevator', 'has_exterior_pool',
                                                             'has_dryer', 'has_spa'),)})
building_services_fieldsets = ('Servicii imobil', {'fields': (
    ('has_administration', 'has_housekeeping', 'has_security', 'has_video_security'),)})
hotel_services_fieldsets = ('Servicii hoteliere', {
    'fields': (('has_cleaning', 'has_bed_sheets', 'has_towels', 'has_station_transfer', 'has_city_tour'),)})
space_other_fieldsets = ('Câmpuri suplimentare', {'fields': (
    'building_year', 'building_stage', 'occupation_degree', ('underground_levels_nr', 'levels_nr'),
    ('has_semi_basement', 'has_ground_floor', 'has_mansard', 'has_terrace', 'has_entresol'),
    'has_parking_possibility', 'parking_spaces_nr', 'building_state')})
space_type_fieldsets = ('Tip spaţiu', {'fields': ('building_type', 'purpose_recommendation')})


#######################################
# Model's admin configs
@admin.register(ApartmentSale)
class ApartmentSaleAdmin(SaleOfferAdmin):
    inlines = (ApartmentSaleImagesInline,)
    apartment_characteristics_fieldsets = ('Caracteristici apartament', {'fields': (
        'apartment_type', 'partitioning_type', 'level', 'comfort', 'util_surface', 'total_util_surface',
        'constructed_surface')})
    building_fieldsets = ('Imobil', {'fields': (
        'building_type', ('has_basement', 'has_semi_basement', 'has_ground_floor', 'levels_nr', 'has_mansard'),
        'building_year', 'building_period', 'resistance_structure'
    )})
    general_utilities_fieldsets = ('Utilităţi generale', {'fields': (
        ('has_current', 'has_water', 'has_sewerage'),
        ('has_gas', 'has_catv', 'has_phone', 'has_international_phone'))})
    other_util_spaces_fieldsets = (
        'Alte spaţii utile', {'fields': (('has_terrace', 'has_service_wc', 'has_basement_box', 'has_storage_closet'),)})

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        SaleOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        price_fieldsets,
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
        SaleOfferAdmin.time_fieldsets
    )


@admin.register(HouseSale)
class HouseSaleAdmin(SaleOfferAdmin):
    inlines = (HouseSaleImagesInline,)
    building_fieldsets = ('Imobil', {'fields': (
        ('has_basement', 'has_semi_basement', 'has_ground_floor', 'levels_nr', 'has_mansard'),
        'building_year', 'building_period', 'resistance_structure', 'roof_cover'
    )})
    surfaces_fieldsets = ('Suprafeţe', {'fields': (
        'util_surface', 'constructed_surface', 'unfolded_surface', 'terrain_surface', 'street_fronts_nr',
        'street_front', 'terrace_nr', 'terrace_surface')})
    general_utilities_fieldsets = ('Utilităţi generale', {'fields': (('has_current', 'has_three_phase_current',
                                                                      'has_water', 'has_sewerage', 'has_septic_tank',
                                                                      'has_gas', 'has_catv', 'has_phone',
                                                                      'has_phone_station',
                                                                      'has_international_phone'),)})
    other_util_spaces = ('Alte spaţii utile', {'fields': (('has_cellar', 'has_wine_cellar', 'has_service_wc',
                                                           'has_storage_space', 'has_dressing', 'has_annexes',
                                                           'has_dependencies'),)})

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        SaleOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        price_fieldsets,
        rooms_fieldsets,
        surfaces_fieldsets,
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
        other_util_spaces,
        kitchen_fieldsets,
        counters_fieldsets,
        furnished_fieldsets,
        appliances_fieldsets,
        diverse_fieldsets,
        building_features_fieldsets,
        building_services_fieldsets,
        hotel_services_fieldsets,
        SaleOfferAdmin.time_fieldsets
    )


@admin.register(LandSale)
class LandSaleAdmin(SaleOfferAdmin):
    inlines = (LandSaleImagesInline,)
    terrain_characteristics_fieldsets = ('Caracteristici teren', {'fields': (
        ('land_type', 'street_fronts_nr'), ('classification', 'street_front'),
        ('terrain_surface', 'terrain_surface_type'), 'terrain_angle', ('pot', 'cut'),
        ('height_regime', 'urban_coefficients_source'), ('constructed_surface', 'access_road_width'),
        'terrain_construction', 'documents', 'plots_lot', 'plots_lot_name')})
    utilities_fieldsets = ('Utilităţi', {'fields': (('has_water', 'has_current', 'has_three_phase_current',
                                                     'has_sewerage', 'has_irrigation_system', 'has_gas',
                                                     'has_utilities_nearby'),)})
    other_characteristics_fieldsets = ('Alte caracteristici', {'fields': (('has_investment_opportunity',
                                                                           'can_be_demolished', 'can_be_splitted',
                                                                           'is_near_road', 'has_auto_access',
                                                                           'is_surrounded_terrain'),)})

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        terrain_characteristics_fieldsets,
        price_fieldsets,
        other_fieldsets,
        destination_fieldsets,
        exclusivity_fieldsets,
        utilities_fieldsets,
        other_zone_details_fieldsets,
        other_characteristics_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )


@admin.register(CommercialSpaceSale)
class CommercialSpaceSaleAdmin(SaleOfferAdmin):
    inlines = (CommercialSpaceSaleImagesInline,)
    property_info_fieldsets = ('Informaţii proprietate', {
        'fields': ('property_name', 'property_description', 'total_surface', 'terrain_surface', 'space_height',
                   'has_show_window')})
    utilities_fieldsets = ('Utilităţi', {
        'fields': (('has_water', 'has_sewerage', 'has_current', 'has_gas', 'has_heating', 'has_conditioning'),)})

    readonly_fields = ['has_ground_floor']
    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        space_other_fieldsets,
        utilities_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        (None, {'fields': ('is_published',)})
    )


@admin.register(OfficeSale)
class OfficeSaleAdmin(SaleOfferAdmin):
    inlines = (OfficeSaleImagesInline,)
    property_info_fieldsets = ('Informaţii proprietate', {
        'fields': ('property_name', 'property_description', 'total_surface', 'office_class', 'terrain_surface')})

    readonly_fields = ['has_ground_floor']
    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        other_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        (None, {'fields': ('is_published',)})
    )


@admin.register(SpecialPropertySale)
class SpecialPropertySaleAdmin(SaleOfferAdmin):
    inlines = (SpecialPropertySaleImagesInline,)


@admin.register(IndustrialSpaceSale)
class IndustrialSpaceSaleAdmin(SaleOfferAdmin):
    inlines = (IndustrialSpaceSaleImagesInline,)
    property_info_fieldsets = ('Informaţii proprietate', {
        'fields': ('property_name', 'property_description', 'total_surface', 'terrain_surface', 'space_height')})
    space_other_fieldsets = ('Câmpuri suplimentare', {'fields': (
        'building_year', 'building_stage', 'occupation_degree', 'levels_nr', 'min_divisible_surface',
        'previous_purpose', 'offices_surface', 'flooring_type', 'resistance_structure', 'platform_surface')})
    utility_fieldsets = ('Utilităţi', {'fields': (('has_water', 'has_gas', 'has_current'),)})
    access_fieldsets = ('Acces', {'fields': (('has_railway', 'has_tir_access', 'has_roads'),)})
    features_fieldsets = ('Dotări', {'fields': (('has_ramp', 'has_slide_bridge', 'has_elevator', 'has_crane',
                                                 'has_heating_installation', 'has_air_conditioning', 'has_windows',
                                                 'has_lighting'),)})

    radio_fields = {'purpose_recommendation': admin.HORIZONTAL}
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        space_type_fieldsets,
        space_price_fieldsets,
        property_info_fieldsets,
        space_other_fieldsets,
        utility_fieldsets,
        access_fieldsets,
        features_fieldsets,
        exclusivity_fieldsets,
        BaseOfferAdmin.time_fieldsets,
        (None, {'fields': ('is_published',)})
    )

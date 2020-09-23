sale_price_fieldsets = ('Preţ', {'fields': (
    ('total_price', 'total_price_currency'), ('util_price', 'util_price_currency'),
    'not_include_vat', 'price_details', 'zero_commission', 'buyer_commission'
)})
rent_price_fieldsets = ('Preţ', {'fields': (
    ('rent_cost', 'rent_currency'),
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
space_utilities_fieldsets = ('Utilităţi', {
    'fields': (('has_water', 'has_sewerage', 'has_current', 'has_gas', 'has_heating', 'has_conditioning'),)})
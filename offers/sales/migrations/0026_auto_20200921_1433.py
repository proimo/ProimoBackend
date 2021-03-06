# Generated by Django 3.1 on 2020-09-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0025_auto_20200920_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='housesale',
            name='asphalted_street',
            field=models.BooleanField(default=False, verbose_name='asfaltate'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='balconies_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. balcoane'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='bathrooms_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. băi'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='building_period',
            field=models.CharField(blank=True, choices=[('_1941', 'Înainte de 1941'), ('1941_1977', 'Între 1941 şi 1977'), ('1977_1990', 'Între 1977 şî 1990'), ('1990_2000', 'Între 1990 şi 2000'), ('2000_2010', 'Între 2000 şi 2010'), ('2010_', 'După 2010')], default=None, max_length=10, verbose_name='perioada construire'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='building_year',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='an finalizare construcţie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='buyer_commission',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='comision cumpărător'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='closed_balconies_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='din care închise'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='concreted_street',
            field=models.BooleanField(default=False, verbose_name='betonate'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='constructed_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţa construită (amprentă la sol) (mp)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='contract',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='housesale',
            name='display_expiry_date',
            field=models.DateTimeField(blank=True, default=None, verbose_name='dată expirare afişare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='disponibility',
            field=models.TextField(blank=True, default=None, verbose_name='disponibilitate proprietate'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='for_offices',
            field=models.BooleanField(default=False, verbose_name='birouri'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='for_vacation',
            field=models.BooleanField(default=False, verbose_name='de vacanţă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='garages_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. garaje'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_administration',
            field=models.BooleanField(default=False, verbose_name='administrare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_air_conditioning',
            field=models.BooleanField(default=False, verbose_name='aer condiţionat'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_air_heater',
            field=models.BooleanField(default=False, verbose_name='aeroterme'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_alarm_system',
            field=models.BooleanField(default=False, verbose_name='sistem de alarmă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_aluminium_rolls',
            field=models.BooleanField(default=False, verbose_name='aluminiu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_aluminium_windows',
            field=models.BooleanField(default=False, verbose_name='aluminiu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_annexes',
            field=models.BooleanField(default=False, verbose_name='anexe'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_auto_access_remote',
            field=models.BooleanField(default=False, verbose_name='telecomandă poartă access auto'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_basement',
            field=models.BooleanField(default=False, verbose_name='are subsol'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_bed_sheets',
            field=models.BooleanField(default=False, verbose_name='lenjerie de pat'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_building_boiler',
            field=models.BooleanField(default=False, verbose_name='centrală imobil'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_carpet_floor',
            field=models.BooleanField(default=False, verbose_name='mochetă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_catv',
            field=models.BooleanField(default=False, verbose_name='CATV'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_cellar',
            field=models.BooleanField(default=False, verbose_name='pivniţă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_cellular_interior_door',
            field=models.BooleanField(default=False, verbose_name='celulare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_chalk_walls',
            field=models.BooleanField(default=False, verbose_name='var'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_city_tour',
            field=models.BooleanField(default=False, verbose_name='tur oraş'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_clay_walls',
            field=models.BooleanField(default=False, verbose_name='humă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_cleaning',
            field=models.BooleanField(default=False, verbose_name='curăţenie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_coffee_maker',
            field=models.BooleanField(default=False, verbose_name='cafetieră'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_common_yard',
            field=models.BooleanField(default=False, verbose_name='curte comună'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_current',
            field=models.BooleanField(default=False, verbose_name='curent'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_decking_floor',
            field=models.BooleanField(default=False, verbose_name='duşumea'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dependencies',
            field=models.BooleanField(default=False, verbose_name='dependinţe'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dial_up',
            field=models.BooleanField(default=False, verbose_name='dial-up'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dishwasher',
            field=models.BooleanField(default=False, verbose_name='maşină de spălat vase'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dressing',
            field=models.BooleanField(default=False, verbose_name='dressing'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dryer',
            field=models.BooleanField(default=False, verbose_name='uscătorie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_dvd',
            field=models.BooleanField(default=False, verbose_name='DVD'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_elevator',
            field=models.BooleanField(default=False, verbose_name='lift'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_equipped_kitchen',
            field=models.BooleanField(default=False, verbose_name='utilată'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_exclusivity',
            field=models.BooleanField(default=False, verbose_name='exclusivitate'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_exterior_pool',
            field=models.BooleanField(default=False, verbose_name='piscină exterioară'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_faience_walls',
            field=models.BooleanField(default=False, verbose_name='faianţă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_fan',
            field=models.BooleanField(default=False, verbose_name='ventiloconvectoare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_fiber',
            field=models.BooleanField(default=False, verbose_name='fibră optică'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_fireplace',
            field=models.BooleanField(default=False, verbose_name='şemineu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_fireplace_or_terracotta',
            field=models.BooleanField(default=False, verbose_name='sobă/teracotă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_flooring_heating',
            field=models.BooleanField(default=False, verbose_name='încălzire prin pardoseală'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_fridge',
            field=models.BooleanField(default=False, verbose_name='frigider'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_furnished_kitchen',
            field=models.BooleanField(default=False, verbose_name='mobilată'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_garage_remote',
            field=models.BooleanField(default=False, verbose_name='telecomandă poartă garaj'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_garden',
            field=models.BooleanField(default=False, verbose_name='grădină'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_gas',
            field=models.BooleanField(default=False, verbose_name='gaz'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_gas_cooker',
            field=models.BooleanField(default=False, verbose_name='aragaz'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_gas_counter',
            field=models.BooleanField(default=False, verbose_name='contor gaz'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_glass_interior_door',
            field=models.BooleanField(default=False, verbose_name='sticlă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_ground_floor',
            field=models.BooleanField(default=True, verbose_name='parter'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_hairdryer',
            field=models.BooleanField(default=False, verbose_name='uscător de păr'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_half_equipped_kitchen',
            field=models.BooleanField(default=False, verbose_name='parţial utilată'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_half_furnished_kitchen',
            field=models.BooleanField(default=False, verbose_name='parţial mobilată'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_heat_counter',
            field=models.BooleanField(default=False, verbose_name='contor căldură'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_heating',
            field=models.BooleanField(default=False, verbose_name='termoficare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_hi_fi',
            field=models.BooleanField(default=False, verbose_name='Hi-Fi'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_hood',
            field=models.BooleanField(default=False, verbose_name='hotă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_horizontal_louver',
            field=models.BooleanField(default=False, verbose_name='orizontale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_housekeeping',
            field=models.BooleanField(default=False, verbose_name='menaj'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_illuminated_street',
            field=models.BooleanField(default=False, verbose_name='iluminat stradal'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_indoor_heat_isolation',
            field=models.BooleanField(default=False, verbose_name='interior'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_intercom',
            field=models.BooleanField(default=False, verbose_name='interfon'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_interior_pool',
            field=models.BooleanField(default=False, verbose_name='piscină interioară'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_interior_stairway',
            field=models.BooleanField(default=False, verbose_name='scară interioară'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_international_phone',
            field=models.BooleanField(default=False, verbose_name='telefon internaţional'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_iron',
            field=models.BooleanField(default=False, verbose_name='fier de călcat'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_jacuzzi',
            field=models.BooleanField(default=False, verbose_name='jacuzzi'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_kitchen_robot',
            field=models.BooleanField(default=False, verbose_name='robot bucătărie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_linoleum_floor',
            field=models.BooleanField(default=False, verbose_name='linoleum'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_mansard',
            field=models.BooleanField(default=False, verbose_name='mansardă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_marble_floor',
            field=models.BooleanField(default=False, verbose_name='marmură'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_metal_entrance_door',
            field=models.BooleanField(default=False, verbose_name='metal'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_outdoor_heat_isolation',
            field=models.BooleanField(default=False, verbose_name='exterior'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_oven',
            field=models.BooleanField(default=False, verbose_name='cuptor cu microunde'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_own_boiler',
            field=models.BooleanField(default=False, verbose_name='centrală proprie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_pal_entrance_door',
            field=models.BooleanField(default=False, verbose_name='pal'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_panel_interior_door',
            field=models.BooleanField(default=False, verbose_name='panel'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_parquet_entrance_door',
            field=models.BooleanField(default=False, verbose_name='parchet'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_parquet_floor',
            field=models.BooleanField(default=False, verbose_name='parchet'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_phone',
            field=models.BooleanField(default=False, verbose_name='telefon'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_phone_station',
            field=models.BooleanField(default=False, verbose_name='centrală telefonică'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_pvc_entrance_door',
            field=models.BooleanField(default=False, verbose_name='PVC'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_pvc_interior_door',
            field=models.BooleanField(default=False, verbose_name='PVC'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_pvc_rolls',
            field=models.BooleanField(default=False, verbose_name='PVC'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_pvc_windows',
            field=models.BooleanField(default=False, verbose_name='PVC'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_radiator',
            field=models.BooleanField(default=False, verbose_name='calorifere'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_recreation_spaces',
            field=models.BooleanField(default=False, verbose_name='spaţii de agrement'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_roof',
            field=models.BooleanField(default=False, verbose_name='acoperiş'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_sandwich_maker',
            field=models.BooleanField(default=False, verbose_name='sandwich-maker'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_sauna',
            field=models.BooleanField(default=False, verbose_name='saună'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_security',
            field=models.BooleanField(default=False, verbose_name='pază'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_semi_basement',
            field=models.BooleanField(default=False, verbose_name='are demisol'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_septic_tank',
            field=models.BooleanField(default=False, verbose_name='fosă septică'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_service_wc',
            field=models.BooleanField(default=False, verbose_name='WC serviciu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_sewerage',
            field=models.BooleanField(default=False, verbose_name='canalizare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_smoke_sensor',
            field=models.BooleanField(default=False, verbose_name='senzor de fum'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_spa',
            field=models.BooleanField(default=False, verbose_name='SPA'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_station_transfer',
            field=models.BooleanField(default=False, verbose_name='transfer aeroport/gară'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_storage_closet',
            field=models.BooleanField(default=False, verbose_name='debara'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_storage_space',
            field=models.BooleanField(default=False, verbose_name='spaţiu depozitare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_three_phase_current',
            field=models.BooleanField(default=False, verbose_name='curent trifazic'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_tiles_floor',
            field=models.BooleanField(default=False, verbose_name='gresie'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_toaster',
            field=models.BooleanField(default=False, verbose_name='toaster'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_towels',
            field=models.BooleanField(default=False, verbose_name='prosoape'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_tv',
            field=models.BooleanField(default=False, verbose_name='tv'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_vacuum_cleaner',
            field=models.BooleanField(default=False, verbose_name='aspirator'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_vertical_louver',
            field=models.BooleanField(default=False, verbose_name='verticale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_video_intercom',
            field=models.BooleanField(default=False, verbose_name='video interfon'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_video_security',
            field=models.BooleanField(default=False, verbose_name='supraveghere video'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_vinarom_walls',
            field=models.BooleanField(default=False, verbose_name='vinarom'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wainscot_walls',
            field=models.BooleanField(default=False, verbose_name='lambriu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wallpaper_walls',
            field=models.BooleanField(default=False, verbose_name='tapet'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wash_machine',
            field=models.BooleanField(default=False, verbose_name='maşină de spălat haine'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_washable_paint_walls',
            field=models.BooleanField(default=False, verbose_name='vopsea lavabilă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_water',
            field=models.BooleanField(default=False, verbose_name='apă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_water_counter',
            field=models.BooleanField(default=False, verbose_name='apometre'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wine_cellar',
            field=models.BooleanField(default=False, verbose_name='cramă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wired_net',
            field=models.BooleanField(default=False, verbose_name='cablu'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wireless',
            field=models.BooleanField(default=False, verbose_name='wireless'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wood_entrance_door',
            field=models.BooleanField(default=False, verbose_name='lemn'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wood_interior_door',
            field=models.BooleanField(default=False, verbose_name='lemn'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wood_rolls',
            field=models.BooleanField(default=False, verbose_name='lemn'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_wood_windows',
            field=models.BooleanField(default=False, verbose_name='lemn'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='has_yard',
            field=models.BooleanField(default=False, verbose_name='curte'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_comercial',
            field=models.BooleanField(default=False, verbose_name='comercial'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_full_furnished',
            field=models.BooleanField(default=False, verbose_name='complet'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_good',
            field=models.BooleanField(default=False, verbose_name='bună'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_half_furnished',
            field=models.BooleanField(default=False, verbose_name='parţial'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_lux_furnished',
            field=models.BooleanField(default=False, verbose_name='lux'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_not_furnished',
            field=models.BooleanField(default=False, verbose_name='nemobilat'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_renovated',
            field=models.BooleanField(default=False, verbose_name='renovat'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='is_residential',
            field=models.BooleanField(default=False, verbose_name='rezidenţial'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='kitchens_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. bucătării'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='levels_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. niveluri'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='need_renovation',
            field=models.BooleanField(default=False, verbose_name='necesită renovare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='not_include_vat',
            field=models.BooleanField(default=False, verbose_name='nu include TVA'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='other_details',
            field=models.TextField(blank=True, default=None, max_length=500, verbose_name='alte detalii'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='parking_lots_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. locuri parcare'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='paved_street',
            field=models.BooleanField(default=False, verbose_name='pietruite'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='price_details',
            field=models.TextField(blank=True, default=None, verbose_name='alte detalii preţ'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='public_transport',
            field=models.BooleanField(default=False, verbose_name='mijloace de transport în comun'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='resistance_structure',
            field=models.CharField(blank=True, choices=[('beton', 'Beton'), ('caramida', 'cărămidă'), ('bca', 'Bca'), ('lemn', 'Lemn'), ('metale', 'Metale'), ('altele', 'Altele')], default=None, max_length=10, verbose_name='structura de rezistenţă'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='roof_cover',
            field=models.CharField(blank=True, choices=[('tabla', 'tablă'), ('tigla', 'ţiglă'), ('sindrila', 'şindrilă')], default=None, max_length=10, verbose_name='învelitoare acoperiş'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='rooms_nr',
            field=models.PositiveIntegerField(default=None, verbose_name='nr. camere'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='soil_street',
            field=models.BooleanField(default=False, verbose_name='de pământ'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='street_front',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='front stradal (m)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='street_fronts_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. fronturi stradale'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='terrace_nr',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='nr. terase'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='terrace_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţă terase (mp)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='terrain_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţă teren (mp)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='preţ total'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='total_price_currency',
            field=models.CharField(choices=[('eur', 'EUR'), ('ron', 'RON'), ('usd', 'USD')], default='eur', max_length=4, verbose_name=''),
        ),
        migrations.AddField(
            model_name='housesale',
            name='undeveloped_street',
            field=models.BooleanField(default=False, verbose_name='neamenajate'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='unfolded_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţă desfăşurată (mp)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='util_price',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='preţ / mp util'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='util_price_currency',
            field=models.CharField(choices=[('eur', 'EUR'), ('ron', 'RON'), ('usd', 'USD')], default='eur', max_length=4, verbose_name=''),
        ),
        migrations.AddField(
            model_name='housesale',
            name='util_surface',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='suprafaţa utilă (mp)'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='validity_from',
            field=models.DateTimeField(blank=True, default=None, verbose_name='valabilitate de la'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='validity_up_to',
            field=models.DateTimeField(blank=True, default=None, verbose_name='până la'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='vices',
            field=models.TextField(blank=True, default=None, max_length=500, verbose_name='vicii'),
        ),
        migrations.AddField(
            model_name='housesale',
            name='zero_commission',
            field=models.BooleanField(default=False, verbose_name='comision 0%'),
        ),
        migrations.AlterField(
            model_name='apartmentsale',
            name='has_semi_basement',
            field=models.BooleanField(default=False, verbose_name='are demisol'),
        ),
    ]

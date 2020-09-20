from django.db.models import BooleanField, URLField, CharField, PositiveIntegerField, TextField, DateTimeField
from offers.choices import ApartmentType, PartitioningType, Level, Comfort, BuildingType, BuildingPeriod, \
    ResistanceStructure, Currencies
from offers.models import OfferImages, BaseOfferModel, WithPrice, WithExclusivity, WithSellingPrice


#######################################
# Base classes
class SaleOfferModel(BaseOfferModel):
    description = TextField('descriere emoţională', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă vânzare'
        verbose_name_plural = 'oferte vânzare'


#######################################
# Model classes
class ApartmentSale(SaleOfferModel, WithSellingPrice, WithExclusivity):
    is_residential_complex = BooleanField('ansamblu rezidenţial', default=False)
    residential_complex_link = URLField(verbose_name="link", blank=True, null=True,
                                        help_text='pagina detalii ansamblu rezidenţial promovat pe imobiliare.ro')

    apartment_type = CharField('tip locuinţă', max_length=11, choices=ApartmentType.choices,
                               default=ApartmentType.APARTAMENT)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)
    util_surface = PositiveIntegerField('suprafaţa utilă (mp)', default=None, blank=True)
    total_util_surface = PositiveIntegerField('suprafaţa utilă totală (mp)', default=None, blank=True)
    constructed_surface = PositiveIntegerField('suprafaţa construită (mp)', default=None, blank=True)

    rooms_nr = PositiveIntegerField('nr. camere', default=None)
    kitchens_nr = PositiveIntegerField('nr. bucătării', blank=True, default=None)
    bathrooms_nr = PositiveIntegerField('nr. băi', blank=True, default=None)
    balconies_nr = PositiveIntegerField('nr. balcoane', blank=True, default=None)
    closed_balconies_nr = PositiveIntegerField('din care închise', blank=True, default=None)
    garages_nr = PositiveIntegerField('nr. garaje', blank=True, default=None)
    parking_lots_nr = PositiveIntegerField('nr. locuri parcare', blank=True, default=None)

    building_type = CharField('tip imobil', max_length=20, choices=BuildingType.choices,
                              default=BuildingType.APARTMENTS_BUILDING)
    has_basement = BooleanField('are subsol', default=False)
    has_semi_basement = BooleanField('Are demisol', default=False)
    has_ground_floor = BooleanField('parter', default=True)
    levels_nr = PositiveIntegerField('nr. niveluri', blank=True, default=None)
    has_mansard = BooleanField('mansardă', default=False)
    building_year = PositiveIntegerField('an finalizare construcţie', blank=True, default=None)
    building_period = CharField('perioada construire', max_length=10, choices=BuildingPeriod.choices, blank=True,
                                default=None)
    resistance_structure = CharField('structura de rezistenţă', max_length=10, choices=ResistanceStructure.choices,
                                     blank=True, default=None)

    other_details = TextField('alte detalii', max_length=500, blank=True, default=None)
    vices = TextField('vicii', max_length=500, blank=True, default=None)
    display_expiry_date = DateTimeField('dată expirare afişare', blank=True, default=None)
    disponibility = TextField('disponibilitate proprietate', blank=True, default=None)

    is_residential = BooleanField('rezidenţial', default=False)
    is_comercial = BooleanField('comercial', default=False)
    for_offices = BooleanField('birouri', default=False)
    for_vacation = BooleanField('de vacanţă', default=False)

    asphalted_street = BooleanField('asfaltate', default=False)
    concreted_street = BooleanField('betonate', default=False)
    paved_street = BooleanField('pietruite', default=False)
    soil_street = BooleanField('de pământ', default=False)
    undeveloped_street = BooleanField('neamenajate', default=False)
    has_illuminated_street = BooleanField('iluminat stradal', default=False)
    public_transport = BooleanField('mijloace de transport în comun', default=False)

    has_current = BooleanField('curent', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_catv = BooleanField('CATV', default=False)
    has_phone = BooleanField('telefon', default=False)
    has_international_phone = BooleanField('telefon internaţional', default=False)

    has_heating = BooleanField('termoficare', default=False)
    has_own_boiler = BooleanField('centrală proprie', default=False)
    has_building_boiler = BooleanField('centrală imobil', default=False)
    has_fireplace_or_terracotta = BooleanField('sobă/teracotă', default=False)
    has_radiator = BooleanField('calorifere', default=False)
    has_flooring_heating = BooleanField('încălzire prin pardoseală', default=False)

    has_air_conditioning = BooleanField('aer condiţionat', default=False)
    has_fan = BooleanField('ventiloconvectoare', default=False)
    has_air_heater = BooleanField('aeroterme', default=False)

    has_wired_net = BooleanField('cablu', default=False)
    has_fiber = BooleanField('fibră optică', default=False)
    has_wireless = BooleanField('wireless', default=False)
    has_dial_up = BooleanField('dial-up', default=False)

    is_renovated = BooleanField('renovat', default=False)
    is_good = BooleanField('bună', default=False)
    need_renovation = BooleanField('necesită renovare', default=False)

    has_aluminium_windows = BooleanField('aluminiu', default=False)
    has_wood_windows = BooleanField('lemn', default=False)
    has_pvc_windows = BooleanField('PVC', default=False)

    has_horizontal_louver = BooleanField('orizontale', default=False)
    has_vertical_louver = BooleanField('verticale', default=False)

    has_pvc_rolls = BooleanField('PVC', default=False)
    has_wood_rolls = BooleanField('lemn', default=False)
    has_aluminium_rolls = BooleanField('aluminiu', default=False)

    has_pal_entrance_door = BooleanField('pal', default=False)
    has_wood_entrance_door = BooleanField('lemn', default=False)
    has_metal_entrance_door = BooleanField('metal', default=False)
    has_pvc_entrance_door = BooleanField('PVC', default=False)
    has_parquet_entrance_door = BooleanField('parchet', default=False)

    has_indoor_heat_isolation = BooleanField('interior', default=False)
    has_outdoor_heat_isolation = BooleanField('exterior', default=False)

    has_linoleum_floor = BooleanField('linoleum', default=False)
    has_carpet_floor = BooleanField('mochetă', default=False)
    has_parquet_floor = BooleanField('parchet', default=False)
    has_tiles_floor = BooleanField('gresie', default=False)
    has_decking_floor = BooleanField('duşumea', default=False)
    has_marble_floor = BooleanField('marmură', default=False)

    has_cellular_interior_door = BooleanField('celulare', default=False)
    has_wood_interior_door = BooleanField('lemn', default=False)
    has_panel_interior_door = BooleanField('panel', default=False)
    has_pvc_interior_door = BooleanField('PVC', default=False)
    has_glass_interior_door = BooleanField('sticlă', default=False)

    has_chalk_walls = BooleanField('var', default=False)
    has_vinarom_walls = BooleanField('vinarom', default=False)
    has_washable_paint_walls = BooleanField('vopsea lavabilă', default=False)
    has_faience_walls = BooleanField('faianţă', default=False)
    has_wainscot_walls = BooleanField('lambriu', default=False)
    has_wallpaper_walls = BooleanField('tapet', default=False)
    has_clay_walls = BooleanField('humă', default=False)

    has_terrace = BooleanField('terasă', default=False)
    has_service_wc = BooleanField('WC serviciu', default=False)
    has_basement_box = BooleanField('boxă la subsol', default=False)
    has_storage_closet = BooleanField('debara', default=False)

    has_furnished_kitchen = BooleanField('mobilată', default=False)
    has_half_furnished_kitchen = BooleanField('parţial mobilată', default=False)
    has_equipped_kitchen = BooleanField('utilată', default=False)
    has_half_equipped_kitchen = BooleanField('parţial utilată', default=False)

    has_gas_counter = BooleanField('contor gaz', default=False)
    has_water_counter = BooleanField('apometre', default=False)
    has_heat_counter = BooleanField('contor căldură', default=False)

    is_not_furnished = BooleanField('nemobilat', default=False)
    is_half_furnished = BooleanField('parţial', default=False)
    is_full_furnished = BooleanField('complet', default=False)
    is_lux_furnished = BooleanField('lux', default=False)

    has_iron = BooleanField('fier de călcat', default=False)
    has_dishwasher = BooleanField('maşină de spălat vase', default=False)
    has_coffee_maker = BooleanField('cafetieră', default=False)
    has_wash_machine = BooleanField('maşină de spălat haine', default=False)
    has_toaster = BooleanField('toaster', default=False)
    has_fridge = BooleanField('frigider', default=False)
    has_oven = BooleanField('cuptor cu microunde', default=False)
    has_gas_cooker = BooleanField('aragaz', default=False)
    has_hood = BooleanField('hotă', default=False)
    has_kitchen_robot = BooleanField('robot bucătărie', default=False)
    has_hairdryer = BooleanField('uscător de păr', default=False)
    has_sandwich_maker = BooleanField('sandwich-maker', default=False)
    has_hi_fi = BooleanField('Hi-Fi', default=False)
    has_tv = BooleanField('tv', default=False)
    has_vacuum_cleaner = BooleanField('aspirator', default=False)
    has_dvd = BooleanField('DVD', default=False)

    has_smoke_sensor = BooleanField('senzor de fum', default=False)
    has_alarm_system = BooleanField('sistem de alarmă', default=False)
    has_fireplace = BooleanField('şemineu', default=False)
    has_jacuzzi = BooleanField('jacuzzi', default=False)
    has_garage_remote = BooleanField('telecomandă poartă garaj', default=False)
    has_auto_access_remote = BooleanField('telecomandă poartă access auto', default=False)
    has_interior_stairway = BooleanField('scară interioară', default=False)

    has_recreation_spaces = BooleanField('spaţii de agrement', default=False)
    has_video_intercom = BooleanField('video interfon', default=False)
    has_interior_pool = BooleanField('piscină interioară', default=False)
    has_sauna = BooleanField('saună', default=False)
    has_roof = BooleanField('acoperiş', default=False)
    has_yard = BooleanField('curte', default=False)
    has_common_yard = BooleanField('curte comună', default=False)
    has_garden = BooleanField('grădină', default=False)
    has_intercom = BooleanField('interfon', default=False)
    has_elevator = BooleanField('lift', default=False)
    has_exterior_pool = BooleanField('piscină exterioară', default=False)
    has_dryer = BooleanField('uscătorie', default=False)
    has_spa = BooleanField('SPA', default=False)

    has_administration = BooleanField('administrare', default=False)
    has_housekeeping = BooleanField('menaj', default=False)
    has_security = BooleanField('pază', default=False)
    has_video_security = BooleanField('supraveghere video', default=False)

    has_cleaning = BooleanField('curăţenie', default=False)
    has_bed_sheets = BooleanField('lenjerie de pat', default=False)
    has_towels = BooleanField('prosoape', default=False)
    has_station_transfer = BooleanField('transfer aeroport/gară', default=False)
    has_city_tour = BooleanField('tur oraş', default=False)

    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseSale(SaleOfferModel):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandSale(SaleOfferModel):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceSale(SaleOfferModel):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeSale(SaleOfferModel):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertySale(SaleOfferModel):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceSale(SaleOfferModel):
    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'


#######################################
# Model classes' images tables
class ApartmentSaleImages(OfferImages):
    foreign_key_name = 'ApartmentSale'


class HouseSaleImages(OfferImages):
    pass


class LandSaleImages(OfferImages):
    pass


class CommercialSpaceSaleImages(OfferImages):
    pass


class OfficeSaleImages(OfferImages):
    pass


class SpecialPropertySaleImages(OfferImages):
    pass


class IndustrialSpaceSaleImages(OfferImages):
    pass

from django.contrib.gis.db.models import PointField, ForeignKey, CharField, BooleanField, SET_NULL, ImageField, CASCADE, \
    Model, TextField, DateTimeField, PositiveIntegerField, IntegerField, DecimalField
from django.db.models.base import ModelBase

from administration.models import UserProfile
from common.models import County, Locality
from common.models import BaseModel
from common.utils import get_upload_path
from offers.choices import Currencies, Sector, BuildingPeriod, ResistanceStructure, BUILDING_STATE, BUILDING_STAGE, \
    PURPOSE_RECOMMENDATION, RoofCover, LandType, LandClassification, SurfaceType, URBAN_COEFF_SOURCES


#######################################
# Base classes both for models and admin
class BaseOfferModel(BaseModel):
    agent = ForeignKey(UserProfile, on_delete=SET_NULL, null=True)
    is_published = BooleanField('publicat?', default=False)
    address = PointField('adresă', max_length=200, null=True)
    hide_address_on_imobiliare = BooleanField('ascunde adresa în imobiliare.ro', default=False)
    county = ForeignKey(County, related_name='%(class)ss', related_query_name='%(class)s', on_delete=SET_NULL,
                        null=True, verbose_name='judeţ')
    locality = ForeignKey(Locality, related_name='%(class)ss', related_query_name='%(class)s', on_delete=SET_NULL,
                          null=True, verbose_name='localitate')
    sector = CharField('sectorul', max_length=2, blank=True, default=None, choices=Sector.choices)
    hide_exact_location_on_imobiliare = BooleanField('ascunde localizarea exactă pe imobiliare.ro', default=False)
    postal_code = CharField('cod poştal', max_length=50, blank=True, default=None)
    neighborhood = CharField('vecinătăţi', max_length=100, blank=True, default=None)
    description = TextField('descriere emoţională', default=None, blank=True)

    class Meta:
        abstract = True


class WithPrice(Model):
    not_include_vat = BooleanField('nu include TVA', default=False)
    price_details = TextField('alte detalii preţ', blank=True, default=None)
    zero_commission = BooleanField('comision 0%', default=False)
    buyer_commission = CharField('comision cumpărător', max_length=50, blank=True, default=None)

    class Meta:
        abstract = True


class WithSellingPrice(WithPrice, Model):
    total_price = PositiveIntegerField('preţ total', blank=True, default=None)
    total_price_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)
    util_price = PositiveIntegerField('preţ / mp util sau UM', blank=True, default=None)
    util_price_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)

    class Meta:
        abstract = True


class WithSpaceSellingPrice(WithPrice, Model):
    price = PositiveIntegerField('preţ cerut', default=None)
    price_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)
    hide_price = BooleanField('nu doresc să fie afişat vizitatorilor site-ului', default=False)

    class Meta:
        abstract = True


class WithPropertyInfo(Model):
    property_name = CharField('nume proprietate', max_length=100, default=None, blank=True)
    property_description = TextField('descriere proprietate', max_length=100, default=None, blank=True)
    total_surface = DecimalField('suprafaţă totală (mp)', max_digits=6, decimal_places=2, default=None)
    terrain_surface = DecimalField('suprafaţă teren (mp)', max_digits=6, decimal_places=2, default=None, blank=True)

    class Meta:
        abstract = True


class WithAdditionalPropertyInfo(Model):
    building_year = PositiveIntegerField('an finalizare construcţie', blank=True, default=None)
    building_stage = CharField('stadiu construcţie', max_length=15, choices=BUILDING_STAGE, default=None, blank=True)
    underground_levels_nr = PositiveIntegerField('nr. niveluri subterane', default=None, blank=True)
    levels_nr = PositiveIntegerField('nr. niveluri', default=None, blank=True)
    has_semi_basement = BooleanField('demisol', default=False)
    has_ground_floor = BooleanField('parter', default=True)
    has_mansard = BooleanField('mansardă', default=False)
    has_terrace = BooleanField('terasă', default=False)
    has_entresol = BooleanField('mezanin', default=False)
    has_parking_possibility = BooleanField('posibilitate parcare', default=False)
    parking_spaces_nr = PositiveIntegerField('nr. locuri parcare', default=None, blank=True)
    building_state = CharField('stare imobil', max_length=15, choices=BUILDING_STATE, default=None, blank=True)

    class Meta:
        abstract = True


class WithSpaceUtilities(Model):
    has_current = BooleanField('curent', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_heating = BooleanField('căldură', default=False)
    has_conditioning = BooleanField('climă', default=False)

    class Meta:
        abstract = True


class WithRecommendation(Model):
    purpose_recommendation = CharField('recomandare utilizare proprietate', max_length=30,
                                       choices=PURPOSE_RECOMMENDATION, default=None, blank=True)

    class Meta:
        abstract = True


class WithRentPrice(WithPrice, Model):
    rent_cost = DecimalField('chirie / lună', max_digits=6, decimal_places=2, blank=True, default=None)
    rent_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)

    class Meta:
        abstract = True


class WithHotelRegime(WithRentPrice, Model):
    hotel_regime = BooleanField('regim hotelier', default=False)
    hotel_regime_price = DecimalField('chirie / zi', max_digits=6, decimal_places=2, blank=True, default=None)
    hotel_regime_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)

    class Meta:
        abstract = True


class WithExclusivity(Model):
    has_exclusivity = BooleanField('exclusivitate', default=False)
    contract = CharField(max_length=200, blank=True, default=None)
    validity_from = DateTimeField('valabilitate de la', blank=True, default=None)
    validity_up_to = DateTimeField('până la', blank=True, default=None)

    class Meta:
        abstract = True


class WithRoomsAndAnnexes(Model):
    rooms_nr = PositiveIntegerField('nr. camere', default=None)
    kitchens_nr = PositiveIntegerField('nr. bucătării', blank=True, default=None)
    bathrooms_nr = PositiveIntegerField('nr. băi', blank=True, default=None)
    balconies_nr = PositiveIntegerField('nr. balcoane', blank=True, default=None)
    closed_balconies_nr = PositiveIntegerField('din care închise', blank=True, default=None)
    garages_nr = PositiveIntegerField('nr. garaje', blank=True, default=None)
    parking_lots_nr = PositiveIntegerField('nr. locuri parcare', blank=True, default=None)

    class Meta:
        abstract = True


class WithHouseSurfaces(Model):
    util_surface = DecimalField('suprafaţa utilă (mp)', max_digits=7, decimal_places=2, default=None, blank=True)
    constructed_surface = DecimalField('suprafaţa construită (amprentă la sol) (mp)', max_digits=7, decimal_places=2,
                                       default=None, blank=True)
    unfolded_surface = DecimalField('suprafaţă desfăşurată (mp)', max_digits=7, decimal_places=2, default=None,
                                    blank=True)
    terrain_surface = DecimalField('suprafaţă teren (mp)', max_digits=7, decimal_places=2, default=None, blank=True)
    street_fronts_nr = PositiveIntegerField('nr. fronturi stradale', default=None, blank=True)
    street_front = DecimalField('front stradal (m)', max_digits=5, decimal_places=2, default=None, blank=True)
    terrace_nr = PositiveIntegerField('nr. terase', default=None, blank=True)
    terrace_surface = DecimalField('suprafaţă terase (mp)', max_digits=6, decimal_places=2, default=None, blank=True)

    class Meta:
        abstract = True


class WithBuildingInfo(Model):
    has_basement = BooleanField('are subsol', default=False)
    has_semi_basement = BooleanField('are demisol', default=False)
    has_ground_floor = BooleanField('parter', default=True)
    levels_nr = PositiveIntegerField('nr. niveluri', blank=True, default=None)
    has_mansard = BooleanField('mansardă', default=False)
    building_year = PositiveIntegerField('an finalizare construcţie', blank=True, default=None)
    building_period = CharField('perioada construire', max_length=10, choices=BuildingPeriod.choices, blank=True,
                                default=None)
    resistance_structure = CharField('structura de rezistenţă', max_length=10, choices=ResistanceStructure.choices,
                                     blank=True, default=None)

    class Meta:
        abstract = True


class WithOtherDetails(Model):
    other_details = TextField('alte detalii', max_length=500, blank=True, default=None)
    vices = TextField('vicii', max_length=500, blank=True, default=None)
    display_expiry_date = DateTimeField('dată expirare afişare', blank=True, default=None)
    disponibility = TextField('disponibilitate proprietate', blank=True, default=None)

    class Meta:
        abstract = True


class WithDestination(Model):
    is_residential = BooleanField('rezidenţial', default=False)
    is_comercial = BooleanField('comercial', default=False)
    for_offices = BooleanField('birouri', default=False)
    for_vacation = BooleanField('de vacanţă', default=False)

    class Meta:
        abstract = True


class WithOtherZoneDetails(Model):
    asphalted_street = BooleanField('asfaltate', default=False)
    concreted_street = BooleanField('betonate', default=False)
    paved_street = BooleanField('pietruite', default=False)
    soil_street = BooleanField('de pământ', default=False)
    undeveloped_street = BooleanField('neamenajate', default=False)
    has_illuminated_street = BooleanField('iluminat stradal', default=False)
    public_transport = BooleanField('mijloace de transport în comun', default=False)

    class Meta:
        abstract = True


class WithHeatingSystem(Model):
    has_heating = BooleanField('termoficare', default=False)
    has_own_boiler = BooleanField('centrală proprie', default=False)
    has_building_boiler = BooleanField('centrală imobil', default=False)
    has_fireplace_or_terracotta = BooleanField('sobă/teracotă', default=False)
    has_radiator = BooleanField('calorifere', default=False)
    has_flooring_heating = BooleanField('încălzire prin pardoseală', default=False)

    class Meta:
        abstract = True


class WithConditioning(Model):
    has_air_conditioning = BooleanField('aer condiţionat', default=False)
    has_fan = BooleanField('ventiloconvectoare', default=False)
    has_air_heater = BooleanField('aeroterme', default=False)

    class Meta:
        abstract = True


class WithFinishes(Model):
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

    class Meta:
        abstract = True


class WithFeatures(Model):
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

    class Meta:
        abstract = True


class WithServices(Model):
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
        abstract = True


class WithInternetAccess(Model):
    has_wired_net = BooleanField('cablu', default=False)
    has_fiber = BooleanField('fibră optică', default=False)
    has_wireless = BooleanField('wireless', default=False)
    has_dial_up = BooleanField('dial-up', default=False)

    class Meta:
        abstract = True


class OfferImagesMetaclass(ModelBase):
    """The class extending OfferImages should get a foreign key to the model"""

    def __new__(mcs, name, bases, attrs):
        model = super(OfferImagesMetaclass, mcs).__new__(mcs, name, bases, attrs)
        for b in bases:
            if b.__name__ == "OfferImages":
                foreign_key_name = attrs.pop('foreign_key_name', None)
                if not foreign_key_name:
                    image_index = name.index('Images')
                    foreign_key_name = name[:image_index]
                has_offer = attrs.pop('offer', None)
                if not has_offer:
                    model.add_to_class('offer', ForeignKey(foreign_key_name, related_name='images', on_delete=CASCADE))

        return model


class OfferImages(Model, metaclass=OfferImagesMetaclass):
    image = ImageField('imagine', upload_to=get_upload_path, blank=True, default=None)

    def __str__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = 'imagine'
        verbose_name_plural = 'imagini'


class HouseBaseModel(BaseOfferModel, WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails,
                     WithDestination, WithExclusivity, WithOtherZoneDetails, WithHeatingSystem, WithConditioning,
                     WithInternetAccess, WithFinishes, WithFeatures, WithServices, WithHouseSurfaces):
    roof_cover = CharField('învelitoare acoperiş', max_length=10, choices=RoofCover.choices, default=None, blank=True)

    has_current = BooleanField('curent', default=False)
    has_three_phase_current = BooleanField('curent trifazic', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_septic_tank = BooleanField('fosă septică', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_catv = BooleanField('CATV', default=False)
    has_phone = BooleanField('telefon', default=False)
    has_phone_station = BooleanField('centrală telefonică', default=False)
    has_international_phone = BooleanField('telefon internaţional', default=False)

    has_cellar = BooleanField('pivniţă', default=False)
    has_wine_cellar = BooleanField('cramă', default=False)
    has_service_wc = BooleanField('WC serviciu', default=False)
    has_storage_space = BooleanField('spaţiu depozitare', default=False)
    has_dressing = BooleanField('dressing', default=False)
    has_annexes = BooleanField('anexe', default=False)
    has_dependencies = BooleanField('dependinţe', default=False)

    class Meta:
        abstract = True


class LandBaseModel(BaseOfferModel, WithOtherDetails, WithDestination, WithExclusivity, WithOtherZoneDetails):
    land_type = CharField('tip teren', max_length=12, choices=LandType.choices, default=LandType.CONSTRUCTII)
    street_fronts_nr = PositiveIntegerField('nr. fronturi stradale', default=None, blank=True)
    classification = CharField('clasificare', max_length=12, choices=LandClassification.choices,
                               default=LandClassification.INTRAVILAN)
    street_front = PositiveIntegerField('front stradal (m)', default=None, blank=True)
    terrain_surface = PositiveIntegerField('suprafaţă teren', default=None, blank=True)
    terrain_surface_type = CharField('', max_length=3, choices=SurfaceType.choices, default=SurfaceType.M)
    terrain_angle = IntegerField('înclinaţie teren (%)', default=None, blank=True)
    pot = IntegerField('P.O.T (%)', default=None, blank=True,
                       help_text='Procentajul de ocupare al terenului (suprafaţa ocupată/suprafaţa totală * 100')
    cut = IntegerField('C.U.T (%)', default=None, blank=True,
                       help_text='Coeficientul de utilizare al terenului (suma suprafeţelor desfăşurate/suprafaţa totală * 100')
    height_regime = PositiveIntegerField('regim înălţime (m)', default=None, blank=True)
    urban_coefficients_source = CharField('sursă informaţii coef. urbanistici', max_length=25,
                                          choices=URBAN_COEFF_SOURCES, default=None, blank=True)
    terrain_construction = BooleanField('construcţie pe teren', default=False)
    constructed_surface = PositiveIntegerField('suprafaţă construită (mp)', default=None, blank=True)
    access_road_width = PositiveIntegerField('lăţime drum de acces (m)', default=None, blank=True)
    documents = TextField('acte/avize', default=None, blank=True)
    plots_lot = BooleanField('lot parcele', default=False)
    plots_lot_name = CharField('nume lot parcele', max_length=100, default=None, blank=True)

    has_current = BooleanField('curent', default=False)
    has_three_phase_current = BooleanField('curent trifazic', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_irrigation_system = BooleanField('sistem irigaţie', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_utilities_nearby = BooleanField('utilităţi în zonă', default=False)

    has_investment_opportunity = BooleanField('oportunitate de investiţie', default=False)
    can_be_demolished = BooleanField('construcţie demolabilă', default=False)
    can_be_splitted = BooleanField('parcelabil', default=False)
    is_near_road = BooleanField('la şosea', default=False)
    has_auto_access = BooleanField('acces auto', default=False)
    is_surrounded_terrain = BooleanField('teren  împrejmuit', default=False)

    class Meta:
        abstract = True

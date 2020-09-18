from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import BooleanField, URLField, CharField, PositiveIntegerField, TextField, DateTimeField

from offers.choices import ApartmentType, PartitioningType, Level, Comfort, BuildingType, BuildingPeriod, \
    ResistanceStructure
from offers.models import OfferImages, BaseOfferModel, WithPrice


#######################################
# Base classes
class SaleOfferModel(BaseOfferModel):
    content = RichTextUploadingField('conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă vânzare'
        verbose_name_plural = 'oferte vânzare'


#######################################
# Model classes
class ApartmentSale(SaleOfferModel, WithPrice):
    is_residential_complex = BooleanField('ansamblu rezidenţial', default=False)
    residential_complex_link = URLField(verbose_name="link", blank=True, null=True,
                                        help_text='pagina detalii ansamblu rezidenţial promovat pe imobiliare.ro')
    hotel_regime = BooleanField('Regim hotelier', default=False)
    apartment_type = CharField('tip locuinţă', max_length=11, choices=ApartmentType.choices,
                               default=ApartmentType.APARTAMENT)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)
    util_surface = CharField('suprafaţa utilă', max_length=50, default=None, blank=True)
    total_util_surface = CharField('suprafaţa utilă totală', max_length=50, default=None, blank=True)
    constructed_surface = CharField('suprafaţa construită', max_length=50, default=None, blank=True)
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
    ground_floor = BooleanField('parter', default=False)
    levels_nr = PositiveIntegerField('nr. niveluri', blank=True, default=None)
    mansard = BooleanField('mansardă', default=False)
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

    has_exclusivity = BooleanField('exclusivitate', default=False)

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
    is_wireless = BooleanField('wireless', default=False)
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

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import PositiveIntegerField, CharField, TextField, Model, DecimalField, DateTimeField, \
    BooleanField, CASCADE, ForeignKey

from offers.choices import Level, Comfort, BuildingType, PartitioningType, OFFICE_BUILDING_TYPE, SPACE_DISPONIBILITY, \
    Currencies, OFFICE_CLASS, COMMERCIAL_BUILDING_TYPE, BUILDING_STATE, INDUSTRIAL_BUILDING_TYPE, FLOORING_TYPE, \
    INDUSTRIAL_RESISTANCE_STRUCTURE, BUILDING_STAGE
from offers.models import OfferImages, BaseOfferModel, WithRentPrice, WithHotelRegime, WithRoomsAndAnnexes, \
    WithHouseSurfaces, WithBuildingInfo, WithOtherDetails, WithDestination, WithExclusivity, HouseBaseModel, \
    LandBaseModel, WithAdditionalPropertyInfo, WithPropertyInfo, WithSpaceUtilities


class SpaceModel(Model):
    name = CharField('denumire spaţiu', max_length=100, default=None, blank=True)
    surface = DecimalField('suprafaţă disponibilă', max_digits=6, decimal_places=2, default=None, blank=True)
    disponibility = CharField('disponibilitate spaţiu', choices=SPACE_DISPONIBILITY, max_length=20, default=None,
                              blank=True)
    disponibility_time = DateTimeField('dată disponibilitate/expirare', default=None, blank=True)
    rent_cost = DecimalField('chirie netă/mp/lună', max_digits=6, decimal_places=2, default=None)
    rent_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)
    hide_price = BooleanField('nu doresc să fie afişat vizitatorilor site-ului', default=False)
    not_include_vat = BooleanField('se adaugă TVA', default=False)
    has_maintenance = BooleanField('se adaugă costuri cu utilităţi/mentenanţă', default=False)
    zero_commission = BooleanField('comision 0%', default=False)
    rent_commission = CharField('comision cerut la închiriere', max_length=50, blank=True, default=None)
    space_height = DecimalField('înalţime spaţiu', max_digits=6, decimal_places=2, default=None, blank=True)
    has_show_window = BooleanField('vitrină', default=False)

    # additional details
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    divisible_space = DecimalField('suprafaţă minimă divizibilă', max_digits=6, decimal_places=2, default=None,
                                   blank=True)
    description = TextField('descriere', max_length=500, default=None, blank=True)
    has_parking = BooleanField('posibilitate parcare', default=False)
    flooring_type = CharField('tip pardoseală', max_length=40, choices=FLOORING_TYPE, default=None, blank=True)
    previous_purpose = CharField('destinaţie anterioară', max_length=100, default=None, blank=True)
    offices_surface = DecimalField('suprafaţă birouri (mp)', max_digits=6, decimal_places=2, default=None, blank=True)
    has_heating_system = BooleanField('instalaţie încălzire', default=False)
    has_air_conditioning = BooleanField('climatizare', default=False)
    has_windows = BooleanField('ferestre/luminatoare', default=False)
    has_lighting = BooleanField('iluminat', default=False)

    # foreign key relations
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = 'spaţiu'
        verbose_name_plural = 'spaţii'


#######################################
# Model classes
class ApartmentRent(BaseOfferModel, WithHotelRegime):
    rooms_nr = PositiveIntegerField('nr. camere', default=0)
    util_surface = CharField('suprafaţa utilă', max_length=50, default=None, blank=True)
    constructed_surface = CharField('suprafaţa construită', max_length=50, default=None, blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    levels_nr = PositiveIntegerField('nr. niveluri', blank=True, default=None)
    building_type = CharField('tip imobil', max_length=20, choices=BuildingType.choices,
                              default=BuildingType.APARTMENTS_BUILDING)
    bathrooms_nr = PositiveIntegerField('nr. băi', blank=True, default=None)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)

    other_details = TextField('alte detalii', max_length=500, blank=True, default=None)

    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseRent(HouseBaseModel, WithHotelRegime):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandRent(LandBaseModel, WithRentPrice):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceRent(BaseOfferModel, WithPropertyInfo, WithAdditionalPropertyInfo, WithSpaceUtilities,
                          WithExclusivity):
    building_type = CharField('tip imobil', max_length=20, choices=COMMERCIAL_BUILDING_TYPE, default=None)
    can_be_partitioned = BooleanField('posibilitate compartimentare', default=False)
    building_state = CharField('stare imobil', max_length=15, choices=BUILDING_STATE, default=None, blank=True)
    spaces = GenericRelation(SpaceModel)

    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeRent(BaseOfferModel, WithPropertyInfo, WithAdditionalPropertyInfo, WithExclusivity):
    building_type = CharField('tip imobil', max_length=20, choices=OFFICE_BUILDING_TYPE, default=None)
    spaces = GenericRelation(SpaceModel)
    office_class = CharField('clasă birouri', max_length=2, choices=OFFICE_CLASS, default=None, blank=True)

    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertyRent(BaseOfferModel, WithPropertyInfo, WithAdditionalPropertyInfo, WithSpaceUtilities,
                          WithExclusivity):
    building_type = CharField('tip proprietate/imobil', max_length=50, default=None)
    building_state = CharField('stare imobil', max_length=15, choices=BUILDING_STATE, default=None, blank=True)
    spaces = GenericRelation(SpaceModel)

    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceRent(BaseOfferModel, WithPropertyInfo, WithExclusivity):
    building_type = CharField('tip proprietate', max_length=50, choices=INDUSTRIAL_BUILDING_TYPE, default=None)
    spaces = GenericRelation(SpaceModel)

    building_year = PositiveIntegerField('an finalizare construcţie', blank=True, default=None)
    building_stage = CharField('stadiu construcţie', max_length=15, choices=BUILDING_STAGE, default=None, blank=True)
    occupation_degree = PositiveIntegerField('grad ocupare clădire (%)', default=None, blank=True)
    levels_nr = PositiveIntegerField('nr. niveluri', default=None, blank=True)
    resistance_structure = CharField('structură rezistenţă', max_length=40, choices=INDUSTRIAL_RESISTANCE_STRUCTURE,
                                     default=None, blank=True)
    platform_surface = DecimalField('suprafaţă platformă (mp)', max_digits=6, decimal_places=2, default=None,
                                    blank=True)

    has_water = BooleanField('apă', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_current = BooleanField('curent', default=False)

    has_railway = BooleanField('cale ferată', default=False)
    has_tir_access = BooleanField('acces tir', default=False)
    has_roads = BooleanField('cale rutieră', default=False)

    has_ramp = BooleanField('rampă', default=False)
    has_slide_bridge = BooleanField('pod rulant', default=False)
    has_elevator = BooleanField('lift', default=False)
    has_crane = BooleanField('macara', default=False)

    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'


#######################################
# Model classes' images tables
class ApartmentRentImages(OfferImages):
    pass


class HouseRentImages(OfferImages):
    pass


class LandRentImages(OfferImages):
    pass


class CommercialSpaceRentImages(OfferImages):
    pass


class OfficeRentImages(OfferImages):
    pass


class SpecialPropertyRentImages(OfferImages):
    pass


class IndustrialSpaceRentImages(OfferImages):
    pass

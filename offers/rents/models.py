from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import PositiveIntegerField, CharField, TextField, Model, DecimalField, DateTimeField, \
    BooleanField, CASCADE, ForeignKey

from offers.choices import Level, Comfort, BuildingType, PartitioningType, OFFICE_BUILDING_TYPE, SPACE_DISPONIBILITY, \
    Currencies, OFFICE_CLASS
from offers.models import OfferImages, BaseOfferModel, WithRentPrice, WithHotelRegime, WithRoomsAndAnnexes, \
    WithHouseSurfaces, WithBuildingInfo, WithOtherDetails, WithDestination, WithExclusivity, HouseBaseModel, \
    LandBaseModel, WithAdditionalPropertyInfo, WithPropertyInfo


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

    # additional details
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    divisible_space = DecimalField('suprafaţă minimă divizibilă', max_digits=6, decimal_places=2, default=None,
                                   blank=True)
    description = TextField('descriere', max_length=500, default=None, blank=True)
    has_parking = BooleanField('posibilitate parcare', default=False)

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


class CommercialSpaceRent(BaseOfferModel):
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


class SpecialPropertyRent(BaseOfferModel):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceRent(BaseOfferModel):
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

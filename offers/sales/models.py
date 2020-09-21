from django.db.models import BooleanField, URLField, CharField, PositiveIntegerField, TextField
from offers.choices import ApartmentType, PartitioningType, Level, Comfort, BuildingType, RoofCover
from offers.models import OfferImages, BaseOfferModel, WithPrice, WithExclusivity, WithSellingPrice, \
    WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails, WithDestination, WithOtherZoneDetails, WithHeatingSystem, \
    WithConditioning, WithInternetAccess, WithFinishes, WithFeatures, WithServices


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
class ApartmentSale(SaleOfferModel, WithSellingPrice, WithExclusivity, WithRoomsAndAnnexes, WithBuildingInfo,
                    WithOtherDetails, WithDestination, WithOtherZoneDetails, WithHeatingSystem, WithConditioning,
                    WithInternetAccess, WithFinishes, WithFeatures, WithServices):
    apartment_type = CharField('tip locuinţă', max_length=11, choices=ApartmentType.choices,
                               default=ApartmentType.APARTAMENT)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)
    util_surface = PositiveIntegerField('suprafaţa utilă (mp)', default=None, blank=True)
    total_util_surface = PositiveIntegerField('suprafaţa utilă totală (mp)', default=None, blank=True)
    constructed_surface = PositiveIntegerField('suprafaţa construită (mp)', default=None, blank=True)

    building_type = CharField('tip imobil', max_length=20, choices=BuildingType.choices,
                              default=BuildingType.APARTMENTS_BUILDING)

    has_current = BooleanField('curent', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_catv = BooleanField('CATV', default=False)
    has_phone = BooleanField('telefon', default=False)
    has_international_phone = BooleanField('telefon internaţional', default=False)

    has_terrace = BooleanField('terasă', default=False)
    has_service_wc = BooleanField('WC serviciu', default=False)
    has_basement_box = BooleanField('boxă la subsol', default=False)
    has_storage_closet = BooleanField('debara', default=False)

    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseSale(SaleOfferModel, WithSellingPrice, WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails,
                WithDestination, WithExclusivity, WithOtherZoneDetails, WithHeatingSystem, WithConditioning,
                WithInternetAccess, WithFinishes, WithFeatures, WithServices):
    util_surface = PositiveIntegerField('suprafaţa utilă (mp)', default=None, blank=True)
    constructed_surface = PositiveIntegerField('suprafaţa construită (amprentă la sol) (mp)', default=None, blank=True)
    unfolded_surface = PositiveIntegerField('suprafaţă desfăşurată (mp)', default=None, blank=True)
    terrain_surface = PositiveIntegerField('suprafaţă teren (mp)', default=None, blank=True)
    street_fronts_nr = PositiveIntegerField('nr. fronturi stradale', default=None, blank=True)
    street_front = PositiveIntegerField('front stradal (m)', default=None, blank=True)
    terrace_nr = PositiveIntegerField('nr. terase', default=None, blank=True)
    terrace_surface = PositiveIntegerField('suprafaţă terase (mp)', default=None, blank=True)

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

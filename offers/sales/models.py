from django.db.models import BooleanField, CharField, PositiveIntegerField, DecimalField
from offers.choices import ApartmentType, PartitioningType, Level, Comfort, BuildingType, OFFICE_BUILDING_TYPE, \
    OFFICE_CLASS, BUILDING_STAGE, COMMERCIAL_BUILDING_TYPE, INDUSTRIAL_BUILDING_TYPE, FLOORING_TYPE, \
    INDUSTRIAL_RESISTANCE_STRUCTURE
from offers.models import OfferImages, BaseOfferModel, WithPrice, WithExclusivity, WithSellingPrice, \
    WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails, WithDestination, WithOtherZoneDetails, WithHeatingSystem, \
    WithConditioning, WithInternetAccess, WithFinishes, WithFeatures, WithServices, WithSpaceSellingPrice, \
    WithPropertyInfo, WithAdditionalPropertyInfo, WithRecommendation, WithSpaceUtilities, WithHouseSurfaces, \
    HouseBaseModel, LandBaseModel


#######################################
# Model classes
class ApartmentSale(BaseOfferModel, WithSellingPrice, WithExclusivity, WithRoomsAndAnnexes, WithBuildingInfo,
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


class HouseSale(HouseBaseModel, WithSellingPrice):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandSale(LandBaseModel, WithSellingPrice):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceSale(BaseOfferModel, WithExclusivity, WithSpaceSellingPrice, WithPropertyInfo,
                          WithAdditionalPropertyInfo, WithRecommendation, WithSpaceUtilities):
    building_type = CharField('tip imobil', max_length=20, choices=COMMERCIAL_BUILDING_TYPE, default=None)
    occupation_degree = PositiveIntegerField('grad ocupare clădire (%)', default=None, blank=True)

    space_height = DecimalField('înalţime spaţiu', max_digits=4, decimal_places=2, default=None, blank=True)
    has_show_window = BooleanField('vitrină', default=False)

    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeSale(BaseOfferModel, WithSpaceSellingPrice, WithOtherDetails, WithExclusivity, WithPropertyInfo,
                 WithAdditionalPropertyInfo, WithRecommendation):
    building_type = CharField('tip imobil', max_length=20, choices=OFFICE_BUILDING_TYPE, default=None)
    occupation_degree = PositiveIntegerField('grad ocupare clădire (%)', default=None, blank=True)
    office_class = CharField('clasă birouri', max_length=2, choices=OFFICE_CLASS, default=None, blank=True)

    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertySale(BaseOfferModel, WithRecommendation, WithSpaceSellingPrice, WithPropertyInfo,
                          WithAdditionalPropertyInfo, WithSpaceUtilities, WithExclusivity):
    building_type = CharField('tip imobil', max_length=100, default=None)
    occupation_degree = PositiveIntegerField('grad ocupare clădire (%)', default=None, blank=True)
    space_height = DecimalField('înalţime spaţiu', max_digits=4, decimal_places=2, default=None, blank=True)

    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceSale(BaseOfferModel, WithRecommendation, WithSpaceSellingPrice, WithPropertyInfo, WithExclusivity):
    building_type = CharField('tip imobil', max_length=20, choices=INDUSTRIAL_BUILDING_TYPE, default=None)

    space_height = DecimalField('înalţime spaţiu', max_digits=4, decimal_places=2, default=None, blank=True)

    building_year = PositiveIntegerField('an finalizare construcţie', blank=True, default=None)
    building_stage = CharField('stadiu construcţie', max_length=15, choices=BUILDING_STAGE, default=None, blank=True)
    occupation_degree = PositiveIntegerField('grad ocupare clădire (%)', default=None, blank=True)
    levels_nr = PositiveIntegerField('nr. niveluri', default=None, blank=True)
    min_divisible_surface = DecimalField('suprafaţă minimă divizabilă (mp)', max_digits=7, decimal_places=2,
                                         default=None, blank=True)
    previous_purpose = CharField('destinaţie anterioară', max_length=100, default=None, blank=True)
    offices_surface = DecimalField('suprafaţă birouri', max_digits=6, decimal_places=2, default=None, blank=True)
    flooring_type = CharField('tip pardoseală', max_length=40, choices=FLOORING_TYPE, default=None, blank=True)
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
    has_heating_installation = BooleanField('instalaţie încălzire', default=False)
    has_air_conditioning = BooleanField('climatizare', default=False)
    has_windows = BooleanField('ferestre/luminatoare', default=False)
    has_lighting = BooleanField('iluminat', default=False)

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

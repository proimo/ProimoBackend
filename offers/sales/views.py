from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale
from offers.sales.serializers import ApartmentSaleSerializer, HouseSaleSerializer, LandSaleSerializer, \
    CommercialSpaceSaleSerializer, OfficeSaleSerializer, SpecialPropertySaleSerializer, IndustrialSpaceSaleSerializer
from offers.views import BaseReadOnlyOfferViewSet


class ApartmentSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = ApartmentSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = ApartmentSaleSerializer


class HouseSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = HouseSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = HouseSaleSerializer


class LandSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = LandSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = LandSaleSerializer


class CommercialSpaceSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = CommercialSpaceSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = CommercialSpaceSaleSerializer


class OfficeSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = OfficeSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = OfficeSaleSerializer


class SpecialPropertySaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = SpecialPropertySale.objects.order_by('-created').filter(is_published=True)
    serializer_class = SpecialPropertySaleSerializer


class IndustrialSpaceSaleViewSet(BaseReadOnlyOfferViewSet):
    queryset = IndustrialSpaceSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = IndustrialSpaceSaleSerializer

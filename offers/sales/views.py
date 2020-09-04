from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale
from offers.sales.serializers import ApartmentSaleSerializer, HouseSaleSerializer, LandSaleSerializer, \
    CommercialSpaceSaleSerializer, OfficeSaleSerializer, SpecialPropertySaleSerializer, IndustrialSpaceSaleSerializer


class BaseReadOnlyOfferViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an offer instance.

        list:
            Return all offers, ordered by most recently add.
    """

    permission_classes = [permissions.AllowAny]


class ApartmentSaleViewSet(ReadOnlyModelViewSet):
    queryset = ApartmentSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = ApartmentSaleSerializer


class HouseSaleViewSet(ReadOnlyModelViewSet):
    queryset = HouseSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = HouseSaleSerializer


class LandSaleViewSet(ReadOnlyModelViewSet):
    queryset = LandSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = LandSaleSerializer


class CommercialSpaceSaleViewSet(ReadOnlyModelViewSet):
    queryset = CommercialSpaceSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = CommercialSpaceSaleSerializer


class OfficeSaleViewSet(ReadOnlyModelViewSet):
    queryset = OfficeSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = OfficeSaleSerializer


class SpecialPropertySaleViewSet(ReadOnlyModelViewSet):
    queryset = SpecialPropertySale.objects.order_by('-created').filter(is_published=True)
    serializer_class = SpecialPropertySaleSerializer


class IndustrialSpaceSaleViewSet(ReadOnlyModelViewSet):
    queryset = IndustrialSpaceSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = IndustrialSpaceSaleSerializer
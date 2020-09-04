from offers.models import BaseReadOnlyOfferViewSet
from offers.rents.models import ApartmentRent, HouseRent, LandRent, CommercialSpaceRent, OfficeRent, \
    SpecialPropertyRent, IndustrialSpaceRent
from offers.rents.serializers import ApartmentRentSerializer, HouseRentSerializer, LandRentSerializer, \
    CommercialSpaceRentSerializer, OfficeRentSerializer, SpecialPropertyRentSerializer, IndustrialSpaceRentSerializer


class ApartmentRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = ApartmentRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = ApartmentRentSerializer


class HouseRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = HouseRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = HouseRentSerializer


class LandRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = LandRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = LandRentSerializer


class CommercialSpaceRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = CommercialSpaceRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = CommercialSpaceRentSerializer


class OfficeRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = OfficeRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = OfficeRentSerializer


class SpecialPropertyRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = SpecialPropertyRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = SpecialPropertyRentSerializer


class IndustrialSpaceRentViewSet(BaseReadOnlyOfferViewSet):
    queryset = IndustrialSpaceRent.objects.order_by('-created').filter(is_published=True)
    serializer_class = IndustrialSpaceRentSerializer

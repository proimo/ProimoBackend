from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from offers.sales.models import ApartmentSale
from offers.sales.serializers import ApartmentSaleSerializer


class ApartmentSaleViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an offer instance.

        list:
            Return all offers, ordered by most recently add.
    """

    queryset = ApartmentSale.objects.order_by('-created').filter(is_published=True)
    serializer_class = ApartmentSaleSerializer
    permission_classes = [permissions.AllowAny]

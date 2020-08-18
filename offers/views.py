from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from offers.models import Offer
from offers.serializers import OfferSerializer


class OfferViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an offer instance.

        list:
            Return all offers, ordered by most recently add.
    """

    queryset = Offer.objects.order_by('-created').filter(published=True)
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]




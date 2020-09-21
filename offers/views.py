#######################################
# Base views class
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet


class BaseReadOnlyOfferViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an offer instance.

        list:
            Return all offers, ordered by most recently add.
    """

    permission_classes = [permissions.AllowAny]

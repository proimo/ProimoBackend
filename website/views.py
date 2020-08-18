from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from website.models import Announcement
from website.serializers import AnnouncementSerializer


class AnnouncementViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an announcement instance.

        list:
            Return all announcements, ordered by most recently add.
    """

    queryset = Announcement.objects.order_by('-created').filter(published=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.AllowAny]




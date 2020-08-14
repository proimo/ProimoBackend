from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from website.models import Announcement, Setting
from website.serializers import AnnouncementSerializer, SettingSerializer


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


class SettingViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return a setting instance.

        list:
            Return all settings.
    """

    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

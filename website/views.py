from rest_framework import viewsets

from website.models import Announcement
from website.serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows announcements to be viewed
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

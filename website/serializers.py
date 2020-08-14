from rest_framework import serializers

from website.models import Announcement


class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'address']

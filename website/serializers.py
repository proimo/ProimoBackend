from rest_framework import serializers

from website.models import Announcement, Setting, AnnouncementImage


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    images = AnnouncementImageSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'region', 'price', 'surface', 'address', 'content', 'images', 'created']


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

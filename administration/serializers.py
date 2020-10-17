from django.db.models import QuerySet
from rest_framework import serializers

from administration.models import Setting, MenuItem


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    @staticmethod
    def get_children(menu_item: MenuItem):
        qs: QuerySet[MenuItem] = MenuItem.objects.filter(is_published=True, parent=menu_item)
        serializer = MenuItemSerializer(instance=qs, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = MenuItem
        fields = '__all__'

from rest_framework import serializers

from administration.models import UserProfile, User
from offers.sales.models import ApartmentSale, ApartmentSaleImages


class ApartmentSaleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentSaleImages
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ApartmentSaleSerializer(serializers.ModelSerializer):
    images = ApartmentSaleImageSerializer(many=True, read_only=True)
    agent = AgentSerializer(read_only=True)

    class Meta:
        model = ApartmentSale
        fields = '__all__'

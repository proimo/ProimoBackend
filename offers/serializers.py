from rest_framework import serializers

from administration.models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class BaseOfferSerializer(serializers.ModelSerializer):
    agent = AgentSerializer(read_only=True)

    class Meta:
        abstract = True
        fields = '__all__'


class BaseImagesSerializers(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

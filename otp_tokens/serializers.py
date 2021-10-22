from rest_framework import serializers
from .models import UserActivation, CardToken, CardVerify


class CardTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardToken
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CardVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardVerify
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserAvtivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivation
        fields = ['otp', 'user']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

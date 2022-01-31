from rest_framework import serializers
from .models import UserActivation, CardToken, CardVerify


class CardTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardToken
        fields = ['card_id', 'otp', 'card_owner', 'hash']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class CardVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardVerify
        fields = ['card_id', 'otp']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
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

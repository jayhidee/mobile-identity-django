from rest_framework import serializers
from .models import TokenMailing, GeneralMail


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenMailing
        fields = ['id', 'email', 'subject', 'message']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralMail
        fields = ['id', 'card', 'user_id',
                  'device', 'uuid', 'action', 'device_ip']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

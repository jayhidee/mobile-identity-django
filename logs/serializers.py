from rest_framework import serializers
from .models import UserAction, CardsLogs


class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        # user_id = serializers.RelatedField(source='user', read_only=True)
        fields = ['user_id', 'action']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class CardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardsLogs
        fields = ['id', 'card', 'user_id', 'time_stamp',
                  'device', 'uuid', 'action', 'device_ip']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

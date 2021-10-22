from rest_framework import serializers
from .models import IssuingOrginization


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuingOrginization
        fields = ['name', 'api', 'email', 'phone_number', 'address']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.api = validated_data.get('api', instance.api)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

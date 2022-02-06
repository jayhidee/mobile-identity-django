from rest_framework import serializers
from .models import VertingOrganization, VertingOrganizationRank, UserOfficer


class VertingOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = VertingOrganization
        fields = ['id', 'name', 'address', 'email',
                  'phone_number']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class VertingOrgRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = VertingOrganizationRank
        fields = ['id', 'name', 'verting_org']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class UserOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOfficer
        fields = ['id', 'user', 'verting_org', 'position']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

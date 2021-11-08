from rest_framework import serializers
from .models import Cards


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        card_id = serializers.CharField(min_length=10)
        # verified = False
        issuing_organization = serializers.CharField(read_only=True,
                                                     source='issuing_organization.id')
        fields = ['id', 'card_id', 'issuing_organization',
                  'date_expiring', 'date_issued']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        # instance = Cards(
        #     card_id=self.validated_data['card_id'],
        #     issuing_organization=self.validated_data['issuing_organization'],
        #     date_expiring=self.validated_data['date_expiring'],
        #     date_issued=self.validated_data['date_issued'],
        #     # verified=False,
        # )
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     instance.card_id = validated_data.get('card_id', instance.card_id)
    #     instance.issuing_organization = validated_data.get(
    #         'issuing_organization', instance.issuing_organization)
    #     instance.date_expiring = validated_data.get(
    #         'date_expiring', instance.date_expiring)
    #     instance.date_issued = validated_data.get(
    #         'date_issued', instance.date_issued)
    #     instance.save()
    #     return instance


class CardOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        card_id = serializers.CharField(min_length=10)
        # verified = False
        # issuing_organization = serializers.CharField(read_only=True,
        #                                              source='IssuingOrginizationOTP.id')
        fields = ['id', 'card_id', 'type', 'issuing_organization', 'first_name', 'last_name',
                  'to_date', 'from_date', 'email', 'phone_number', 'date_approved', 'approved', 'reason_for_visit']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

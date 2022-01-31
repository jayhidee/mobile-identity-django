import json
from django.core.checks import messages
from django.db.models.fields import DateTimeField
from django.template import context
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from requests.api import delete
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token
import requests


from organization.models import IssuingOrginization
from .serializers import CardSerializer, CardOTPSerializer, CardOfflineSerializer
from .models import Cards, CardsOTP, CardsOffline
from logs.internal import UserAction
from otp_tokens.views import CardToken, OTP, otp_card
from otp_tokens.models import CardToken
from otp_tokens.serializers import CardTokenSerializer
import datetime

import qrcode
import qrcode.image.svg
from io import BytesIO


class Cardz(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # return Response(request.data)
        cardsss = Cards(user_id=request.user, verified=False)
        serializer = CardSerializer(cardsss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User created a new card (" + request.data['card_id'] + ")")

        return Response({"message": "Your card has been added please do verify card"})

    def get(self, request):
        org = Cards.objects.filter(user_id=request.user).select_related(
            'issuing_organization').values_list('card_id', 'date_expiring', 'date_issued', 'id', 'issuing_organization__name', 'issuing_organization__images')
        serializer = CardSerializer(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User viewed list of his card")
        return Response(org)


class CardzD(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, id, *args, **kwargs):
        data = request.data

        qs = Cards.objects.get(id=id)
        serializer = CardSerializer(instance=qs, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User edited his card (" + request.data['card_id'] + ")")
        return Response({"message": "Card has been edited please verify card again"})

    def put(self, request, id, *args, **kwargs):
        # Run some API verification
        Cards.objects.filter(id=id).update(Verified=True)

    def get(self, request, id):
        qs = Cards.objects.filter(id=id)
        serializer = CardSerializer(qs, many=True)
        return Response(serializer.data)


# Get token

class CardzView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id, card_id, *args, **kwargs):
        qs = Cards.objects.filter(card_id=card_id)
        if qs:
            UserAction.objects.create(
                user_id=request.user, action="User viewed his card with ID("+card_id + ")")

            cardsss = CardToken(card_owner=request.user)
            hash = {
                "card_id": id,
                "otp": OTP(),
                "card_owner": request.user.id
            }
            salted = make_password(json.dumps(hash))
            newCardToken = {
                "card_id": id,
                "otp": OTP(),
                "card_owner": request.user.id,
                "hash": salted
            }
            serializer = CardTokenSerializer(data=newCardToken)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"message": salted})
        else:
            return Response({"message": "Card with ID not found"})


class CardValidate(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token_validity = CardToken.objects.filter(
            card_id=request.data['card_id'],  valied=True, date_expiring__gte=datetime.datetime.now())
        if token_validity:
            card_det = Cards.objects.filter(
                id=request.data['card_id']).select_related('issuing_organization').values_list('card_id', 'issuing_organization__name')
            user_det = Cards.objects.filter(
                id=request.data['card_id']).select_related('user_id').values_list('user_id__first_name', 'user_id__last_name')
            if card_det:
                data = {
                    "name": user_det,
                    "success": True,
                    "card_id": card_det,
                }
                CardToken.objects.update(
                    valied=False, date_used=datetime.datetime.now(), officer=request.user.id)
                return Response(data)
            else:
                return Response({"success": False, "message": "Invalid Card ID"})
        else:
            return Response({"success": False, "message": "Token is Invalid"})


class CardOTP(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        card_idz = otp_card()
        crd = CardsOTP.objects.filter(card_id=card_idz)
        if crd:
            card_idzz = otp_card()
            request.data['card_id'] = card_idzz
            request.data['approved'] = False
            cardsss = CardsOTP(requested_by=request.user)
            serializer = CardOTPSerializer(cardsss, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # user action Log
            UserAction.objects.create(
                user_id=request.user, action="User requested a new access (" + card_idzz + ")")
            return Response({"message": "Your request has been received please wait for aproval."})

        else:
            request.data['card_id'] = card_idz
            request.data['approved'] = False
            cardsss = CardsOTP(requested_by=request.user)
            serializer = CardOTPSerializer(cardsss, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # user action Log
            UserAction.objects.create(
                user_id=request.user, action="User requested a new access (" + card_idz + ")")
            return Response({"success": True, "message": "Your request has been received please wait for aproval."})

    def get(self, request):
        uz = request.user
        crd = CardsOTP.objects.filter(requested_by=uz)
        serializer = CardOTPSerializer(crd, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User viewed list of his one time access")
        return Response(serializer.data)


class DownloadCard(APIView):
    # aqrcode-7.3.1uthentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        cardz = Cards.objects.filter(user_id=request.user, card_id=request.data['card_id']).select_related(
            'issuing_organization').values_list('card_id', 'date_expiring', 'date_issued', 'id', 'issuing_organization__name', 'issuing_organization__images')

        d = list(cardz)

        findCard = CardsOffline.objects.filter(
            deleted=False, user_id=request.user)

        findOff = CardsOffline.objects.filter(
            card_id=d[0][3], deleted=False, user_id=request.user)

        if findCard:
            return Response({"success": "false", "message": "You can only have one ofline card"})
        elif findOff:
            fullname = request.user.get_full_name()
            data = CardOfflineSerializer(findOff, many=True)
            return Response({"success": "true", "message": d, "name": fullname})
        else:
            CardsOffline.objects.create(
                card_id=d[0][3], user_id=request.user, image="blank", last_download=datetime.datetime.now(), created=True, deleted=False)
            return Response({"success": "true", "message": d, "name": request.user.get_full_name()})

    def get(self, request):
        card = CardsOffline.objects.filter(user_id=request.user)
        data = CardOfflineSerializer(card, many=True)
        if not card:
            return Response({"success": "false", "message": "No offline card available"})
        else:
            return Response({"success": "true", "message": data.data})


class DownloaddCard(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        card = CardsOffline.objects.get(
            user_id=request.user, id=request.data['card_id'])
        data = CardOfflineSerializer(card, many=True)
        return Response({"message": data.data})


class DownloadDeleteCard(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        card = CardsOffline.objects.filter(
            user_id=request.user, deleted=False, id=id)
        data = CardOfflineSerializer(card, many=True)
        if not card:
            return Response({"message": "card has been deleted"})
        else:
            return Response({"message": data.data})

    def delete(self, request, id):
        checkForID = Cards.objects.filter(user_id=request.user, id=id)

        if not checkForID:
            return Response({"success": "false", "message": "Invalid Card selected"})
        else:
            CardsOffline.objects.filter(card_id=id).update(deleted=True)
            return Response({"success": "true", "message": "Card has been deleted"})


class GenerateQRCode(APIView):
    def get(self, request, salted):
        context = {}
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(
            salted, image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        return render(request, 'download_card.html', context=context)

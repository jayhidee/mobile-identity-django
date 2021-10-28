from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token


from .serializers import CardSerializer
from .models import Cards
from logs.internal import UserAction
from otp_tokens.views import CardToken
from otp_tokens.models import CardToken
import jwt
import datetime


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
        org = Cards.objects.filter(user_id=request.user)
        serializer = CardSerializer(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User viewed list of his card")
        return Response(serializer.data)


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

    def get(self, id):
        qs = Cards.objects.filter(id=id)
        serializer = CardSerializer(qs, many=True)
        return Response(serializer.data)


class CardzView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id, *args, **kwargs):
        qs = Cards.objects.filter(card_id=id)
        if qs:
            newCardToken = {
                "card_id": id,
                "card_owner": request.user,
                "otp": ""
            }
            UserAction.objects.create(
                user_id=request.user, action="User viewed his card with ID("+id+")")
            return CardToken(newCardToken)
        else:
            return Response({"message": "Card with ID not found"})


class CardValidate(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token_validity = CardToken.object.filter(
            card_id=request.data['card_id'],  valid=True)
        if token_validity['date_expiring'] > datetime.datetime.now():
            return True
        else:
            return Response({"message": "Token is Invalid"})

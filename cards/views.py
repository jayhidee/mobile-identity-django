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
import jwt
import datetime


class Cardz(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        cardsss = Cards(user_id=request.user, verified=False)
        serializer = CardSerializer(cardsss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User created a new card (" + request.data['card_id'] + ")")
        return Response(serializer.data)

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
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        # Run some API verification
        Cards.objects.filter(id=id).update(Verified=True)

    def post(self, id):
        pass

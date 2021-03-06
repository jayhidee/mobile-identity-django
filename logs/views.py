from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token


from .serializers import CardLogSerializer, UserLogSerializer, ErrorLogSerializer
from .models import CardsLogs, UserAction as Act
from logs.internal import UserAction
import jwt
import datetime


class CardLogs(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        log = CardsLogs.objects.filter(card=id)
        serializer = CardLogSerializer(log, many=True)
        return Response(serializer.data)


class CardLogsPost(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # return Response(request.data)
        # cardsss = CardsLogs(user_id=request.user)
        request.data['user_id'] = request.user.id
        serializer = CardLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User generated new token for his card")
        return Response({"message": "Token generated"})

    def get(self, request):
        log = Act.objects.filter(user_id=request.user)
        serializer = UserLogSerializer(log, many=True)
        return Response(serializer.data)


def errorHandeling(logs):
    serializer = ErrorLogSerializer(data=logs)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return True

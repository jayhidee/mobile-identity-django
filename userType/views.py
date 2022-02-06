import json
from django.db.models.fields import DateTimeField
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token
import requests


from .serializers import VertingOrgSerializer, VertingOrgRankSerializer, UserOfficerSerializer
from .models import UserOfficer, VertingOrganization, VertingOrganizationRank
from logs.internal import UserAction
from otp_tokens.views import CardToken, OTP, otp_card
from otp_tokens.models import CardToken
from otp_tokens.serializers import CardTokenSerializer
import datetime


class VertingOrgView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = VertingOrgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Created Verting Organization (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request):
        vert = VertingOrganization.objects.all()
        serializer = VertingOrgSerializer(vert, many=True)
        return Response(serializer.data)


class VertingOrgDView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, id, *args, **kwargs):
        qs = VertingOrganization.objects.get(id=id)
        serializer = VertingOrgSerializer(instance=qs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Edited Verting Organization (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request, id, *args, **kwargs):
        vert = VertingOrganization.objects.filter(id=id)
        serializer = VertingOrgSerializer(vert, many=True)
        return Response(serializer.data)


class VertingRankOrgView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = VertingOrgRankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Created Verting Organization Rank (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request):
        vert = VertingOrganizationRank.objects.all()
        serializer = VertingOrgRankSerializer(vert, many=True)
        return Response(serializer.data)


class VertingOrgRankDView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, id, *args, **kwargs):
        qs = VertingOrganizationRank.objects.get(id=id)
        serializer = VertingOrgRankSerializer(instance=qs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Edited Verting Organization (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request, id, *args, **kwargs):
        vert = VertingOrganizationRank.objects.filter(id=id)
        serializer = VertingOrgRankSerializer(vert, many=True)
        return Response(serializer.data)

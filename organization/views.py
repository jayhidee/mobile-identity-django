from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token


from .serializers import OrgSerializer, OrgSerializerO
from .models import IssuingOrginization, IssuingOrginizationOTP
from logs.models import UserAction


class IssOrg(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = OrgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Created Organization (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request):
        org = IssuingOrginization.objects.all()
        serializer = OrgSerializer(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User viewed the list of organization")
        return Response(serializer.data)


class IssOrgD(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, id, *args, **kwargs):
        data = request.data
        qs = IssuingOrginization.objects.get(id=id)
        serializer = OrgSerializer(instance=qs, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Edited Organization (" + qs.name + ")")
        return Response(serializer.data)

    def get(self, request, id, *args, **kwargs):
        org = IssuingOrginization.objects.filter(id=id)
        serializer = OrgSerializer(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Viewed Organization ")
        return Response(serializer.data)


class IssOrgO(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = OrgSerializerO(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Created Organization (" + request.data['name'] + ")")
        return Response(serializer.data)

    def get(self, request):
        org = IssuingOrginizationOTP.objects.all()
        serializer = OrgSerializerO(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User viewed the list of organization")
        return Response(serializer.data)


class IssOrgDO(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, id, *args, **kwargs):
        data = request.data
        qs = IssuingOrginizationOTP.objects.get(id=id)
        serializer = OrgSerializerO(instance=qs, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Edited Organization (" + qs.name + ")")
        return Response(serializer.data)

    def get(self, request, id, *args, **kwargs):
        org = IssuingOrginizationOTP.objects.filter(id=id)
        serializer = OrgSerializerO(org, many=True)
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User Viewed Organization ")
        return Response(serializer.data)

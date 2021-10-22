import math
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .serializers import UserAvtivationSerializer, CardTokenSerializer, CardVerifySerializer
from .models import UserActivation, CardToken, CardVerify
from logs.models import UserAction
from mailing_service.views import ToksMail


def UseAct(request):
    oyp = OTP()
    request['otp'] = oyp
    serializer = UserAvtivationSerializer(data=request)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # Mail
    mail_html = render_to_string(
        "token_mail.html", {'url': 'https://nameless-retreat-73704.herokuapp.com/api/one-time-pass/account-activation/', 'emailz': request['email'], 'namez': request['name'], 'token': oyp})
    text = strip_tags(mail_html)
    mailer = {
        'subject': 'User Activation Token',
        'message': mail_html,
        'email': request['email']
    }
    return ToksMail(mailer)
    # return Response(serializer.data)


def OTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

   # length of password can be changed
   # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


class UserAct(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = UserAvtivationSerializer(data=request.data)
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

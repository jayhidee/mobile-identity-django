from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication, permissions, serializers
from rest_framework.authtoken.models import Token

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.utils.html import strip_tags

from .serializers import TokenSerializer, GeneralSerializer
from .models import TokenMailing, GeneralMail
from logs.models import UserAction


def ToksMail(request):
    newSend = [request['email']]
    text = text = strip_tags(request['message'])
    x = send_mail(
        subject=request['subject'],
        message=text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=newSend,
        html_message=request['message']
    )
    if x:
        serializers = TokenSerializer(data=request)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return True
    else:
        return False


class Gen(APIView):
    authentication_classes = (authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated)

    def post(self, request):
        message = "Test"
        subject = "subject"
        email = "idowujohn9@gmail.com"
        from_mail = ["test@codedtee.com"]

        send_mail(
            subject,
            message,
            from_mail,
            email
        )
        serializers = GeneralSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({'message': 'Mail sent'})

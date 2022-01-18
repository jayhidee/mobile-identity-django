from django.core.checks import messages
from django.db.models.fields import DateTimeField
from django.template.loader import render_to_string
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
import imgkit


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
            newCardToken = {
                "card_id": id,
                "otp": OTP(),
                "card_owner": request.user.id
            }
            serializer = CardTokenSerializer(data=newCardToken)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
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
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        cardz = Cards.objects.filter(user_id=request.user, card_id=request.data['card_id']).select_related(
            'issuing_organization').values_list('card_id', 'date_expiring', 'date_issued', 'id', 'issuing_organization__name', 'issuing_organization__images')

        d = list(cardz)
        findOff = CardsOffline.objects.filter(
            card_id=d[0][3], deleted=False, user_id=request.user)

        if findOff:
            data = CardOfflineSerializer(findOff, many=True)
            return Response({"message": data.data})
        else:
            id_num = d[0][0]
            name = request.user.get_full_name()
            iss_org = d[0][4]

            image = """
                        <html>
                            <head>



                                <!--Fontawesome-->
                                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

                                <!-- Bootstrap core CSS -->
                                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
                                <style>
                                # cs{
                                    width: 40vw;
                                    height: auto;
                                    margin: auto;
                                    background-image: url(https://res.cloudinary.com/gims/image/upload/v1639396599/int-pass_ud28p9.png);
                                    background-position: center;
                                    background-repeat: no-repeat;
                                    background-size: cover;
                                }
                                body{
                                    background: transparent;
                                }
                                </style>
                            </head>

                            <body>
                                <div class="card p-5 m-auto" id="cs">
                                    <div class="card-body container">
                                    <div class="row m-auto">
                                        <span class="col-2">
                                        jj
                                        </span>
                                        <span class="col-10">
                                        <h3><strong>Federal Republic of Nigeria</strong></h3>
                                        </span>
                                    </div>
                                    <div class="row py-5 m-auto">
                                        <div class="col-4">
                                        <img class="img-fluid" src="https://cdn.pixabay.com/photo/2015/03/04/22/35/head-659652_960_720.png">
                                        <span></span>
                                        </div>
                                        <div class="col-8 my-4">
                                        <h4><strong>ID:</strong>  %s</h4>
                                        <h4><strong>Name:</strong> %s</h4>
                                        <h4><strong>Age:</strong>  40</h4>
                                        <h4><strong>Address:</strong>  This a test address that can change</h4>
                                        <h4><strong>Sex:</strong>  M</h4>
                                        </div>
                                    </div>
                                    <div class="row m-auto">
                                        <span class="col-12 text-center">
                                        <i class=""><small>%s<br>Federal Republic of Nigeria</small></i>
                                        </span>
                                    </div>
                                </div>
                                </div>



                                <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
                                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
                                <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
                            </body>
                        </html>

                    """ % (id_num, name, iss_org)
            HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
            # Retrieve these from https://htmlcsstoimage.com/dashboard
            HCTI_API_USER_ID = '64046e10-8be7-4e35-b6ea-180706dd73fd'
            HCTI_API_KEY = '7995399a-e729-4287-be06-b7a3b78e0a2b'

            data = {'html': image,
                    'css': ".box { color: white; background: transparent; padding: 10px; font-family: Roboto }#cs{ width: 40vw; height: auto;  margin: auto; background-size: cover; background-image: url(https://res.cloudinary.com/gims/image/upload/v1639396599/int-pass_ud28p9.png); background-position: center; background-repeat: no-repeat; }",
                    'google_fonts': "Roboto"}
            dd = requests.post(url=HCTI_API_ENDPOINT, data=data,
                               auth=(HCTI_API_USER_ID, HCTI_API_KEY))

            CardsOffline.objects.create(
                card_id=d[0][3], user_id=request.user, image=dd.json()['url'], last_download=datetime.datetime.now(), created=True, deleted=False)

            return Response({"download": dd.json()['url']})

    def get(self, request):
        card = CardsOffline.objects.filter(user_id=request.user)
        data = CardOfflineSerializer(card, many=True)
        if not card:
            return Response({"message": "No offline card available"})
        else:
            return Response({"message": data.data})


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
        pass

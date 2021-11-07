from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token


from .serializers import UserSerializer
from .models import User
from otp_tokens.views import UseAct
from logs.internal import UserAction


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        res = {
            'otp': '',
            'user': serializer.data['id'],
            'email': request.data['email'],
            'name': request.data['first_name'] + " " + request.data['last_name']
        }
        # user action Log
        UserAction.objects.create(
            user_id=serializer.data, action="User create a new account")

        if UseAct(res) == True:
            return Response({'message': 'Thanks for regestring. Please check your mail to activate your account.'})
        else:
            return Response({'message': 'Thanks for regestring. Please Try requesting for token again'})


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect email or password!')

        # Token Check
        if Token.objects.filter(user=user):
            token = Token.objects.get(user=user)

            response = Response()
            # if
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'token': token.key,
                'success': 'ture',
                'user': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }
            }
            # user action Log
            UserAction.objects.create(
                user_id=user, action="User logged in")

            return response
        else:
            token = Token.objects.create(user=user)

            response = Response()
            # if
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'token': token.key,
                'success': 'ture',
                'user': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }
            }
            # user action Log
            UserAction.objects.create(
                user_id=user, action="User logged in")

            return response


class LogoutView(APIView):

    @permission_classes([IsAuthenticated])
    def get(self, request):
        # user action Log
        UserAction.objects.create(
            user_id=request.user, action="User logged out")

        # request.user.auth_token.delete()
        # logout(request)
        return Response({"message": "Thanks. Hope to see you again"})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token


from .serializers import UserSerializer
from .models import User
from otp_tokens.views import UseAct


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        res = {
            'otp': '',
            'user': 1,
            'email': request.data['email'],
            'name': request.data['first_name'] + " " + request.data['last_name']
        }
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

        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }

        # token = jwt.encode(payload, 'secret',
        #                    algorithm='HS256').decode('utf-8')

        token = Token.objects.create(user=user)

        response = Response()

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
        return response


class LogoutView(APIView):

    @permission_classes([IsAuthenticated])
    def post(self, request):
        response = Response()
        # response.delete_cookie('jwt')
        Token.delete(user=request.user)
        response.data = {
            'message': 'success'
        }
        return response

from rest_framework.serializers import Serializer
from .models import UserAction, CardsLogs
from .serializers import UserLogSerializer


def createUser(action):
    serializer = UserLogSerializer(data=action)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return True


def createLog(action):
    serializer = UserLogSerializer(data=action)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return True

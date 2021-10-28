from django.urls import path
from .views import CardLogs

urlpatterns = [
    path('', CardLogs.as_view()),
]

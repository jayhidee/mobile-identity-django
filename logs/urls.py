from django.urls import path
from .views import CardLogs

urlpatterns = [
    path('<str:id>', CardLogs.as_view()),
]

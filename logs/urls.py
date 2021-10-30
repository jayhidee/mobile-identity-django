from django.urls import path
from .views import CardLogs, CardLogsPost

urlpatterns = [
    path('<str:id>', CardLogs.as_view()),
    path('', CardLogsPost.as_view()),
]

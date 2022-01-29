from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CreateGroups, UnlockView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('unlock', UnlockView.as_view()),
    path('logout', LogoutView.as_view()),
    path('groups', CreateGroups.as_view()),
]

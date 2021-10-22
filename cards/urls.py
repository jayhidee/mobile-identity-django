from django.urls import path
from .views import Cardz, CardzD

urlpatterns = [
    path('', Cardz.as_view()),
    path('<int:id>', CardzD.as_view()),
]

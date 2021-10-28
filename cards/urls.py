from django.urls import path
from .views import Cardz, CardzD, CardzView, CardValidate

urlpatterns = [
    path('', Cardz.as_view()),
    path('<int:id>', CardzD.as_view()),
    path('view/<str:id>', CardzView.as_view()),
    path('validate/', CardValidate.as_view()),
]

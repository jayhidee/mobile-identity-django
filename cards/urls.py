from django.urls import path
from .views import Cardz, CardzD, CardzView, CardValidate, CardOTP, DownloadCard, DownloadDeleteCard

urlpatterns = [
    path('', Cardz.as_view()),
    path('<int:id>', CardzD.as_view()),
    path('view/<str:card_id>/<int:id>/', CardzView.as_view()),
    path('validate/', CardValidate.as_view()),
    path('otp/', CardOTP.as_view()),
    path('get-card/', DownloadCard.as_view()),
    path('offline-card/<int:id>/', DownloadDeleteCard.as_view()),
]

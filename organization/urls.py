from django.urls import path
from .views import IssOrg, IssOrgD, IssOrgO, IssOrgDO

urlpatterns = [
    path('', IssOrg.as_view()),
    path('<int:id>', IssOrgD.as_view()),
    path('otp/', IssOrgO.as_view()),
    path('otp/<int:id>', IssOrgDO.as_view()),
]

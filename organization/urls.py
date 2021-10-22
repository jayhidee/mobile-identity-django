from django.urls import path
from .views import IssOrg, IssOrgD

urlpatterns = [
    path('', IssOrg.as_view()),
    path('<int:id>', IssOrgD.as_view()),
]

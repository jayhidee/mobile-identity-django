from django.urls import path
from .views import VertingOrgDView, VertingOrgView, VertingOrgRankDView, VertingRankOrgView

urlpatterns = [
    path('verting', VertingOrgView.as_view()),
    path('verting/<int:id>', VertingOrgDView.as_view()),
    path('verting/position', VertingRankOrgView.as_view()),
    path('verting/position/<int:id>', VertingOrgRankDView.as_view()),
]

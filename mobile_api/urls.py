"""mobile_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('user.urls')),
    path('api/org/', include('organization.urls')),
    path('api/cards/', include('cards.urls')),
    path('api/logs/', include('logs.urls')),
    path("robots.txt", TemplateView.as_view(
        template_name="templates/robots.txt", content_type="text/plain")),
]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'
handler503 = 'utils.views.error_503'
handler403 = 'utils.views.error_403'

from django.contrib import admin
from .models import CardsLogs, UserAction, ErrorLogging

# Register your models here.

admin.site.register(CardsLogs)
admin.site.register(UserAction)
admin.site.register(ErrorLogging)

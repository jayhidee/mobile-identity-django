from django.contrib import admin
from .models import TokenMailing, GeneralMail

# Register your models here.

admin.site.register(TokenMailing)
admin.site.register(GeneralMail)

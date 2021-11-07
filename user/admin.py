from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'firstName', 'lastName']

    class Meta:
        model = User


# Register your models here.
admin.site.register(User, UserAdmin)

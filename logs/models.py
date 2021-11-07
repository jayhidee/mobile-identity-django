from django.db import models
from user.models import User
from cards.models import Cards

# Create your models here.


class UserAction(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.TextField(max_length=255)

    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return self.card_id


# Create your models here.
class CardsLogs(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.PROTECT)
    time_stamp = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    device = models.CharField(max_length=100)
    uuid = models.UUIDField(editable=False, null=True)
    action = models.TextField(max_length=255)
    device_ip = models.GenericIPAddressField(null=True)
    device_os = models.CharField(max_length=100)

    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return self.card


class ErrorLogging(models.Model):
    code = models.CharField(max_length=255)
    error_type = models.CharField(max_length=255)
    error_details = models.TextField()
    time_field = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['time_field']

    def __str__(self):
        return self.code

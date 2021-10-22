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
    uuid = models.UUIDField(editable=False)
    action = models.TextField(max_length=255)
    device_ip = models.GenericIPAddressField()

    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return self.card

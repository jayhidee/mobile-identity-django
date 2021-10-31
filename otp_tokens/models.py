from django.db import models
from user.models import User
from cards.models import Cards
from datetime import datetime, timedelta


# Create your models here.


class CardToken(models.Model):
    card_id = models.ForeignKey(Cards, on_delete=models.PROTECT)
    otp = models.CharField(max_length=20)
    card_owner = models.ForeignKey(User, on_delete=models.PROTECT)
    officer = models.IntegerField(null=True)
    date_used = models.DateTimeField(null=True)
    valied = models.BooleanField(default=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_expiring = models.DateTimeField(
        default=datetime.now()+timedelta(minutes=60))

    class Meta:
        ordering = ['date_used']

    def __str__(self):
        return self.card_id


class CardVerify(models.Model):
    card_id = models.ForeignKey(Cards, on_delete=models.PROTECT)
    otp = models.CharField(max_length=20)
    card_owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_used = models.DateTimeField(null=True)
    valied = models.BooleanField(default=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_expiring = models.DateTimeField(
        default=datetime.now()+timedelta(minutes=6))

    class Meta:
        ordering = ['date_used']

    def __str__(self):
        return self.card_id


class UserActivation(models.Model):
    otp = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_used = models.DateTimeField(null=True)
    valied = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_used']

    def __str__(self):
        return self.otp

from django.db import models
from user.models import User
from cards.models import Cards
from datetime import datetime, timedelta
from django.utils import timezone


# Create your models here.


class CardToken(models.Model):
    card_id = models.ForeignKey(Cards, on_delete=models.PROTECT)
    otp = models.CharField(max_length=20)
    hash = models.CharField(max_length=220, default='s')
    card_owner = models.ForeignKey(User, on_delete=models.PROTECT)
    officer = models.IntegerField(null=True)
    date_used = models.DateTimeField(null=True)
    valied = models.BooleanField(default=True)
    date_issued = models.DateTimeField(default=timezone.now())
    date_expiring = models.DateTimeField(
        default=datetime.now() + timedelta(hours=0, minutes=6, seconds=0))

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

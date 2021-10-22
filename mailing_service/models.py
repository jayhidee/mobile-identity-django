from django.db import models
from user.models import User

# Create your models here.


class TokenMailing(models.Model):
    email = models.CharField(max_length=255)
    subject = models.TextField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email


class GeneralMail(models.Model):
    email = models.CharField(max_length=255)
    subject = models.TextField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

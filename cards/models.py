from django.db import models
from organization.models import IssuingOrginization
from user.models import User

# Create your models here.


class Cards(models.Model):
    card_id = models.CharField(max_length=255, unique=True)
    issuing_organization = models.ForeignKey(
        IssuingOrginization, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    date_expiring = models.DateField()
    date_issued = models.DateField()
    verified = models.BooleanField()

    class Meta:
        ordering = ['date_issued']

    def __str__(self):
        return self.card_id

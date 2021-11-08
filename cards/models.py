from django.db import models
from organization.models import IssuingOrginization, IssuingOrginizationOTP
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


class CardsOTP(models.Model):
    card_id = models.CharField(max_length=255, unique=True)
    issuing_organization = models.ForeignKey(
        IssuingOrginizationOTP, on_delete=models.PROTECT)
    type = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,)
    from_date = models.DateField()
    to_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    date_approved = models.DateField()
    approved = models.BooleanField()
    approved_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="approved_by", null=True)
    reason_for_visit = models.TextField()
    requested_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="requested_by")

    class Meta:
        ordering = ['date_approved']

    def __str__(self):
        return self.card_id

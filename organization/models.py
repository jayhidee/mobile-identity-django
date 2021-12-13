from django.db import models

# Create your models here.


class IssuingOrginization(models.Model):
    name = models.CharField(max_length=255)
    api = models.URLField()
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    images = models.URLField(null=True, default='https://test.com')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class IssuingOrginizationOTP(models.Model):
    name = models.CharField(max_length=255)
    api = models.URLField()
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    images = models.URLField(null=True, default='https://test.com')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

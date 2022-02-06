from django.db import models
from user.models import User


class VertingOrganization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class VertingOrganizationRank(models.Model):
    name = models.CharField(max_length=255)
    verting_org = models.ForeignKey(
        VertingOrganization, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class UserOfficer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    verting_org = models.ForeignKey(
        VertingOrganization, on_delete=models.PROTECT)
    position = models.ForeignKey(
        VertingOrganizationRank, on_delete=models.PROTECT)

    class Meta:
        ordering = ['verting_org']

    def __str__(self):
        return self.user

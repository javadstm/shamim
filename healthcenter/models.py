from django.contrib.auth.models import User
from django.db import models


class Details(models.Model):
    rank = models.CharField(max_length=64, blank=True)


class HealthCenterModels(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    state = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(max_length=64, blank=True, null=True)
    Details = models.ManyToManyField(Details)


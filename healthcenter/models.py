from django.contrib.auth.models import User
from django.db import models


class Details(models.Model):
    rank = models.CharField(max_length=64, blank=True)


class state(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class city(models.Model):
    name = models.CharField(max_length=64)
    state = models.ForeignKey(state, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HealthCenterModels(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    manager = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.TextField()
    state = models.ForeignKey(state, blank=True, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(city, blank=True, null=True, on_delete=models.SET_NULL)
    Details = models.ManyToManyField(Details)
    lat = models.CharField(max_length=64, null=True, blank=True)
    long = models.CharField(max_length=64, null=True, blank=True)

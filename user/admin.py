from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from healthcenter.models import state, city


@register(state)
class StateAdmin(admin.ModelAdmin):
    pass


@register(city)
class RegionAdmin(admin.ModelAdmin):
    pass

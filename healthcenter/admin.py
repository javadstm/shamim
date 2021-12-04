from django.contrib import admin
from healthcenter.models import HealthCenterModels


# Register your models here.

class HealthCenterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_by', 'address', 'state', 'region']
    list_filter = ['region', 'state']
    search_fields = ['region', 'state']


admin.site.register(HealthCenterModels, HealthCenterModelAdmin)

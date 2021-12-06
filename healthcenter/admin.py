from django.contrib import admin
from healthcenter.models import HealthCenterModels


# Register your models here.

class HealthCenterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_by', 'address', 'state', 'city']
    list_filter = ['city', 'state']
    search_fields = ['city', 'state']


admin.site.register(HealthCenterModels, HealthCenterModelAdmin)




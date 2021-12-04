import django_filters
from .models import HealthCenterModels


class healthfilter(django_filters.FilterSet):
    class Meta:
        model = HealthCenterModels
        fields = ['state', 'region']

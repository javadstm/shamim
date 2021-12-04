from django.forms import ModelForm
from .models import HealthCenterModels


class CreateCenterform(ModelForm):
    class Meta:
        model = HealthCenterModels
        fields = '__all__'
        exclude = ('Details',)
        # manager can be still there to be chosen
        # exclude = ('manager',)

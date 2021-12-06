from django.forms import ModelForm
from .models import HealthCenterModels, state, city


class CreateCenterform(ModelForm):
    class Meta:
        model = HealthCenterModels
        fields = '__all__'
        exclude = ('Details', 'created_by',)

        # manager can be still there to be chosen
        # exclude = ('manager',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city'].queryset = city.objects.none()

            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('country'))
                    self.fields['city'].queryset = city.objects.filter(state_id=state_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

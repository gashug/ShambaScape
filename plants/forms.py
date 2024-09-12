from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'description', 'category', 'sun_exposure', 'water_requirements', 'soil_requirements', 'bloom_time', 'harvest_time']
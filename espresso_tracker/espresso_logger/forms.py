from django import forms
from .models import CoffeeLog

class CoffeeLogForm(forms.ModelForm):
    class Meta:
        model = CoffeeLog
        fields = '__all__'

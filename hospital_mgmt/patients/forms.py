from django import forms
from .models import Patient

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['symptoms', 'history']

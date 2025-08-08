from django import forms
from .models import Appointment
from doctors.models import Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor','date','time','reason']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only approved doctors visible
        self.fields['doctor'].queryset = Doctor.objects.filter(approved=True)

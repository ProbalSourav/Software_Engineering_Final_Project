from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'room_charge', 'doctor_fee', 'medicine_cost', 'other_cost', 'notes']

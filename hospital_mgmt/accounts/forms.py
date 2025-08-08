from django import forms
from django.contrib.auth.models import User

class PatientSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    symptoms = forms.CharField(widget=forms.Textarea, label='Initial symptoms')
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class DoctorSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    specialization = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PatientSignupForm, DoctorSignupForm
from .models import Profile
from patients.models import Patient
from doctors.models import Doctor

def home(request):
    return render(request, 'home.html')

def signup_patient(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            Profile.objects.create(user=user, role='Patient', approved=False)
            Patient.objects.create(user=user, symptoms=form.cleaned_data['symptoms'])
            return redirect('login')
    else:
        form = PatientSignupForm()
    return render(request, 'accounts/signup_patient.html', {'form': form})

def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            Profile.objects.create(user=user, role='Doctor', approved=False)
            Doctor.objects.create(user=user, specialization=form.cleaned_data['specialization'])
            return redirect('login')
    else:
        form = DoctorSignupForm()
    return render(request, 'accounts/signup_doctor.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('post_login_redirect')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def post_login_redirect(request):
    profile = getattr(request.user, 'profile', None)
    if profile:
        if profile.role == 'Admin':
            return redirect('admin_dashboard')
        if profile.role == 'Doctor':
            return redirect('doctor_dashboard')
        if profile.role == 'Patient':
            return redirect('patient_dashboard')
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')

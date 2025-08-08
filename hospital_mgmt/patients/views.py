from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.utils import role_required
from .models import Patient
from appointments.models import Appointment
from billing.models import Bill

@login_required
@role_required('Patient')
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date', '-time')
    bills = Bill.objects.filter(patient=patient).order_by('-created_at')
    return render(request, 'patients/dashboard.html', {'patient': patient, 'appointments': appointments, 'bills': bills})

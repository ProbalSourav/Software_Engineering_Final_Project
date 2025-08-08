from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.utils import role_required
from .forms import AppointmentForm
from .models import Appointment
from patients.models import Patient

@login_required
@role_required('Patient')
def create_appointment(request):
    patient = Patient.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = patient
            appt.status = 'Pending'
            try:
                appt.full_clean()
                appt.save()
                messages.success(request, "Appointment request submitted.")
                return redirect('patient_dashboard')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': form})

@login_required
@role_required('Patient')
def cancel_appointment(request, pk):
    patient = Patient.objects.get(user=request.user)
    appt = get_object_or_404(Appointment, pk=pk, patient=patient)
    appt.status = 'Cancelled'
    appt.save()
    return redirect('patient_dashboard')

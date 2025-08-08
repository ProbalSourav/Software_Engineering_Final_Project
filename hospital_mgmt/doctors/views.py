from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.utils import role_required
from .models import Doctor
from appointments.models import Appointment
from patients.models import Patient

@login_required
@role_required('Doctor')
def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date','time')
    return render(request, 'doctors/dashboard.html', {'doctor': doctor, 'appointments': appointments})

@login_required
@role_required('Doctor')
def appointment_set_status(request, pk, status):
    doctor = Doctor.objects.get(user=request.user)
    appt = get_object_or_404(Appointment, pk=pk, doctor=doctor)
    if status in ['Approved','Declined']:
        appt.status = status
        appt.save()
    return redirect('doctor_dashboard')

@login_required
@role_required('Doctor')
def patient_record(request, patient_id):
    doctor = Doctor.objects.get(user=request.user)
    patient = get_object_or_404(Patient, pk=patient_id)
    # In real systems, you'd enforce assignment; simplified for demo
    appts = Appointment.objects.filter(doctor=doctor, patient=patient)
    return render(request, 'doctors/patient_record.html', {'patient': patient, 'appts': appts})

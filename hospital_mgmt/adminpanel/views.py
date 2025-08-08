from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.utils import role_required
from accounts.models import Profile
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

@login_required
@role_required('Admin')
def admin_dashboard(request):
    stats = {
        'patients_pending': Patient.objects.filter(approved=False).count(),
        'doctors_pending': Doctor.objects.filter(approved=False).count(),
        'appointments_pending': Appointment.objects.filter(status='Pending').count(),
        'appointments_today': Appointment.objects.filter(date=date.today()).count(),
    }
    return render(request, 'adminpanel/dashboard.html', {'stats': stats})

@login_required
@role_required('Admin')
def approvals(request):
    pending_patients = Patient.objects.filter(approved=False)
    pending_doctors = Doctor.objects.filter(approved=False)
    return render(request, 'adminpanel/approvals.html', {'pending_patients': pending_patients, 'pending_doctors': pending_doctors})

@login_required
@role_required('Admin')
def approve_patient(request, pk):
    p = get_object_or_404(Patient, pk=pk)
    p.approved = True
    p.save()
    prof = p.user.profile
    prof.approved = True
    prof.save()
    return redirect('approvals')

@login_required
@role_required('Admin')
def approve_doctor(request, pk):
    d = get_object_or_404(Doctor, pk=pk)
    d.approved = True
    d.save()
    prof = d.user.profile
    prof.approved = True
    prof.save()
    return redirect('approvals')

@login_required
@role_required('Admin')
def discharge_patient(request, pk):
    p = get_object_or_404(Patient, pk=pk)
    p.is_discharged = True
    p.discharge_date = date.today()
    p.save()
    return redirect('admin_dashboard')

@login_required
@role_required('Admin')
def appointments_overview(request):
    appts = Appointment.objects.select_related('patient__user','doctor__user').order_by('-date','-time')
    return render(request, 'adminpanel/appointments.html', {'appointments': appts})

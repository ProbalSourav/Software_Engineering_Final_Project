import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.utils import role_required
from .forms import BillForm
from .models import Bill

@login_required
@role_required('Admin')
def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_billing_list')
    else:
        form = BillForm()
    return render(request, 'billing/create.html', {'form': form})

@login_required
@role_required('Admin')
def billing_list(request):
    bills = Bill.objects.select_related('patient','patient__user').order_by('-created_at')
    return render(request, 'billing/list.html', {'bills': bills})

@login_required
@role_required('Patient')
def my_bills(request):
    bills = Bill.objects.filter(patient__user=request.user).order_by('-created_at')
    return render(request, 'billing/my_bills.html', {'bills': bills})

@login_required
def download_bill_csv(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    # Only owner patient, admin, or staff can download
    user = request.user
    allowed = False
    if hasattr(user, 'profile'):
        role = user.profile.role
        if role == 'Admin':
            allowed = True
        elif role == 'Patient' and bill.patient.user_id == user.id:
            allowed = True
    if not allowed:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename=bill_{bill.pk}.csv'
    writer = csv.writer(response)
    writer.writerow(['Bill ID', bill.pk])
    writer.writerow(['Patient', bill.patient.user.get_full_name() or bill.patient.user.username])
    writer.writerow(['Room Charge', bill.room_charge])
    writer.writerow(['Doctor Fee', bill.doctor_fee])
    writer.writerow(['Medicine Cost', bill.medicine_cost])
    writer.writerow(['Other Cost', bill.other_cost])
    writer.writerow(['Total', bill.total])
    writer.writerow(['Notes', bill.notes])
    return response

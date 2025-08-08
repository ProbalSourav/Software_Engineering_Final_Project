from django.urls import path
from .views import admin_dashboard, approvals, approve_patient, approve_doctor, discharge_patient, appointments_overview

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approvals/', approvals, name='approvals'),
    path('approve/patient/<int:pk>/', approve_patient, name='approve_patient'),
    path('approve/doctor/<int:pk>/', approve_doctor, name='approve_doctor'),
    path('discharge/<int:pk>/', discharge_patient, name='discharge_patient'),
    path('appointments/', appointments_overview, name='appointments_overview'),
]
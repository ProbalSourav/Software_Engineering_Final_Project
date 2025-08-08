from django.urls import path
from .views import doctor_dashboard, appointment_set_status, patient_record

urlpatterns = [
    path('dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('appointments/<int:pk>/<str:status>/', appointment_set_status, name='doctor_appointment_set_status'),
    path('patient/<int:patient_id>/', patient_record, name='doctor_patient_record'),
]

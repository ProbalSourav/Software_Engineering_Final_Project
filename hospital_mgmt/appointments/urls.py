from django.urls import path
from .views import create_appointment, cancel_appointment

urlpatterns = [
    path('create/', create_appointment, name='create_appointment'),
    path('cancel/<int:pk>/', cancel_appointment, name='cancel_appointment'),
]

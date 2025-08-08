from django.urls import path
from .views import create_bill, billing_list, my_bills, download_bill_csv

urlpatterns = [
    path('create/', create_bill, name='create_bill'),
    path('admin/list/', billing_list, name='admin_billing_list'),
    path('me/', my_bills, name='my_bills'),
    path('download/<int:pk>/', download_bill_csv, name='download_bill'),
]

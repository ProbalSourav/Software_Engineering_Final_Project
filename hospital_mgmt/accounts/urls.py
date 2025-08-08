from django.urls import path
from .views import signup_patient, signup_doctor, login_view, logout_view, post_login_redirect

urlpatterns = [
    path('signup/patient/', signup_patient, name='signup_patient'),
    path('signup/doctor/', signup_doctor, name='signup_doctor'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('redirect/', post_login_redirect, name='post_login_redirect'),
]

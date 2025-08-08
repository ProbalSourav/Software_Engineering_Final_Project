from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    symptoms = models.TextField()
    approved = models.BooleanField(default=False)  # mirrors Profile.approved (for convenience)
    is_discharged = models.BooleanField(default=False)
    discharge_date = models.DateField(null=True, blank=True)
    history = models.TextField(blank=True, default='')

    def __str__(self):
        return self.user.username

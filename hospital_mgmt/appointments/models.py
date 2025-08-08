from django.db import models
from django.core.exceptions import ValidationError

class Appointment(models.Model):
    STATUS = (('Pending','Pending'), ('Approved','Approved'), ('Declined','Declined'), ('Cancelled','Cancelled'))
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'date', 'time')

    def clean(self):
        # conflict detection: prevent double booking at the same slot
        if Appointment.objects.exclude(pk=self.pk).filter(doctor=self.doctor, date=self.date, time=self.time, status__in=['Pending','Approved']).exists():
            raise ValidationError("This time slot is not available for the selected doctor.")

    def __str__(self):
        return f"{self.date} {self.time} - {self.patient} with {self.doctor}"

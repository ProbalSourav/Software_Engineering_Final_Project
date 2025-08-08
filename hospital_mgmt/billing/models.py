from django.db import models

class Bill(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='bills')
    room_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    doctor_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medicine_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def compute_total(self):
        self.total = (self.room_charge or 0) + (self.doctor_fee or 0) + (self.medicine_cost or 0) + (self.other_cost or 0)

    def save(self, *args, **kwargs):
        self.compute_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.pk} - {self.patient}"

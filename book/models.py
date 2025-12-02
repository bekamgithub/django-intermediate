from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    SERVICE_TYPES = [
        ("Consultation", "Consultation"),
        ("Repair", "Repair"),
        ("Meeting", "Meeting"),
        ("Training", "Training"),
        ("Other", "Other"),
    ]

    STATUS_TYPES = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
]


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=20, choices=SERVICE_TYPES)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES, default="Pending")

    def __str__(self):
        return f"{self.name} - {self.service}"



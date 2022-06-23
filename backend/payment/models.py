from django.db import models
from hostel.models import TrackingModel

# Create your models here.
PAYMENT_MODES= [
    ('mpesa', 'Mpesa'),
    ('paypal', 'Paypal'),
    ]


class Payment(TrackingModel):
    student_id = models.CharField(max_length=30, default='')
    first_name= models.CharField(max_length=100, default='')
    last_name= models.CharField(max_length=100, default='')
    room_id = models.CharField(max_length=20, default='')
    room_charge = models.FloatField(null=False, default=0.0)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey('Room', on_delete = models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add = True)
    checking_date = models.DateTimeField(blank = True, null=True)
    checkout_date = models.DateTimeField(null = True, blank = True)
    phone_number = models.CharField(max_length = 14, null = True)
    email = models.EmailField()
    
    def __str__(self):
        return self.customer.username
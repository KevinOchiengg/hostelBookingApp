from django.db import models
from hostel.models import Hostel

class Room(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20,blank=False,null=False)
    max_occupants = models.IntegerField(blank=False,null=False)
    room_available = models.BooleanField(default=True)
    room_price = models.BigIntegerField(blank=False,null=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.hostel,self.room_number)

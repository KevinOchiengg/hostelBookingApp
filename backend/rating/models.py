from django.db import models
from user.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from hostel.models import Hostel,TrackingModel

class Rating(TrackingModel):
 
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE )
    hostel = models.ForeignKey(Hostel , on_delete=models.CASCADE )
    subject = models.CharField(max_length=10, default='optional')
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
 
    def __str__(self) -> str:
        return self.subject

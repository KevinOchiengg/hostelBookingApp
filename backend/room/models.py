from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from hostel.models import Hostel
#from rating.models import Rating
# Create your models here.


class Room(models.Model):
    category = [
        ("single", "S"),
        ("double", "D"),
        ("multiple", "M")
    ]
    number = models.IntegerField(primary_key=True, validators=[
        MaxValueValidator(1000),
        MinValueValidator(0)
    ])
    #hostel_name = models.ForeignKey(Hostel, max_length=20, on_delete=models.CASCADE)
   # rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=category, null=True)
    capacity = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    price = models.IntegerField(default=0, validators=[
        MaxValueValidator(5000),
        MinValueValidator(0)
    ])
    no_of_beds = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    vacancy = models.BooleanField(default=False)

    #def __str__(self):
        #return "%s %s" % (self.hostel_name, self.number)

from django.db import models
from django.contrib.auth.models import User

class flights(models.Model):
    Source=models.CharField(max_length=15)
    destination=models.CharField(max_length=15)
    Start=models.CharField(max_length=10,default='10:00')
    End=models.CharField(max_length=10,default='10:00')
    Price=models.IntegerField(default=2000)


class Booking(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    source=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    booking_date=models.DateTimeField()
    journey_date=models.DateField()
    price=models.CharField(max_length=10)
    mob=models.CharField(max_length=11)
    booked_by=models.ForeignKey(User,on_delete=models.CASCADE)

from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Airport(models.Model):
    name = models.CharField(max_length=70)
    country = CountryField()
    airport_code = models.CharField(max_length=3)

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name


class Flight(models.Model):
    aeroplane = models.CharField(max_length=28)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin")
    destination= models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure_datetime = models.DateField(default=timezone.now)
    arrival_datetime = models.DateField(default=timezone.now)
    max_passenger = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def duration(self):
        duration_difference = self.arrival_datetime - self.departure_datetime
        hours = round(duration_difference.total_seconds() / 3600)
        return f"{hours}hours"
    
    def __str__(self):
        return self.aeroplane
    
   # def get_absolute_url(self):
       # return reverse("flight:booking_flight", args=[self.flight])


class Booking(models.Model):
    reference_no = models.CharField(max_length=6, unique=True)
    passenger_first_name = models.CharField(max_length=70, blank=True)
    passenger_last_name = models.CharField(max_length=70, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)      
    booking_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.reference_no


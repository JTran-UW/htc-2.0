from django.db import models
from users.models import User

# Create your models here.

class Vehicle(models.TextChoices):
    CAR = "Car/Van"
    TRUCK = "Truck"

class PricingModel(models.TextChoices):
    MILE = "Per Mile"
    HOUR = "Per Hour"

class RideOffer(models.Model):
    """
    Django model for ride offer
    """
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Logistics
    vehicle_type = models.CharField(max_length=10, choices=Vehicle.choices, default=Vehicle.CAR)
    location = models.CharField(max_length=20)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pricing_model = models.CharField(max_length=10, choices=PricingModel.choices, default=PricingModel.MILE)
    price = models.FloatField()
    max_load = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    description = models.TextField()

class RideRequest(models.Model):
    """
    Request for a ride
    """
    business = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Logistics
    vehicle_type = models.CharField(max_length=10, choices=Vehicle.choices, default=Vehicle.CAR)
    location = models.CharField(max_length=20)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pricing_model = models.CharField(max_length=10, choices=PricingModel.choices, default=PricingModel.MILE)
    price = models.FloatField()
    max_load = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    description = models.TextField()
    
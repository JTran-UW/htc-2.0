from django.db import models
from users.models import User

# Create your models here.

class RideOffer(models.Model):
    """
    Django model for ride offer
    """
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_to_end = models.DateTimeField()
    description = models.TextField()

class RideRequest(models.Model):
    """
    Request for a ride
    """
    business = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_to_end = models.DateTimeField()
    description = models.TextField()

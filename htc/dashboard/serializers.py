from rest_framework import serializers
from .models import RideOffer, RideRequest

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideOffer
        fields = ('driver', 'date_created', 'duration', 'description')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('business', 'date_created', 'duration', 'description')

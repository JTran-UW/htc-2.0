from rest_framework import serializers
from .models import RideOffer, RideRequest

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideOffer
        fields = ('driver', 'date_created', 'vehicle_type', 'location', 'begin_date', 'end_date', 'pricing_model', 'price', 'max_load', 'size', 'description')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('business', 'date_created', 'vehicle_type', 'location', 'begin_date', 'end_date', 'pricing_model', 'price', 'max_load', 'size', 'description')

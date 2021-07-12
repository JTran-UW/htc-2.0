from django.forms import ModelForm
from .models import RideOffer, RideRequest

class OfferForm(ModelForm):
    class Meta:
        model = RideOffer
        fields = ["driver", "vehicle_type", "location", "begin_date", "end_date", "pricing_model", "price", "max_load", "size", "description"]

class RequestForm(ModelForm):
    class Meta:
        model = RideRequest
        fields = ["business", "vehicle_type", "location", "begin_date", "end_date", "pricing_model", "price", "max_load", "size", "description"]

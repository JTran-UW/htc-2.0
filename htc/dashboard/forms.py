from django.forms import ModelForm
from .models import RideOffer, RideRequest

class OfferForm(ModelForm):
    class Meta:
        model = RideOffer
        fields = ["driver", "date_to_end", "description"]

class RequestForm(ModelForm):
    class Meta:
        model = RideRequest
        fields = ["business", "date_to_end", "description"]

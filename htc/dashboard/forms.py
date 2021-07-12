from django import forms
from .models import RideOffer, RideRequest

class DateInput(forms.DateInput):
    input_type = 'date'

class OfferForm(forms.ModelForm):
    class Meta:
        model = RideOffer
        fields = ["vehicle_type", "location", "begin_date", "end_date", "pricing_model", "price", "max_load", "size", "description"]
        widgets = {
            "begin_date": DateInput(),
            "end_date": DateInput()
        }

class RequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = ["vehicle_type", "location", "begin_date", "end_date", "pricing_model", "price", "max_load", "size", "description"]
        widgets = {
            "begin_date": DateInput(),
            "end_date": DateInput()
        }

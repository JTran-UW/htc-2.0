from .models import RideOffer
from rest_framework import viewsets
from .serializers import OfferSerializer, RequestSerializer
from .models import RideOffer, RideRequest

# Create your views here.

class OfferView(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = RideOffer.objects.all()

class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = RideRequest.objects.all()

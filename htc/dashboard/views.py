from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OfferForm
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

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def offer(request):
    if request.method == "POST":
        request.POST["driver"] = request.user
        form = OfferForm(request.POST)
        if form.is_valid():
            new_offer = RideOffer.objects.create(
                driver = request.user,
                date_to_end = request.POST["date_to_end"],
                description = request.POST["descrition"]
            )
            new_offer.save
    
    form = OfferForm()
    return render(request, "dashboard/offer.html", {"form": form})

@login_required
def rent(request):
    return render(request, "dashboard/rent.html")

@login_required
def request_ride(request):
    return render(request, "dashboard/request.html")

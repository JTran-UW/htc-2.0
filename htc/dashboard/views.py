from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OfferForm, RequestForm
from .models import RideOffer, RideRequest

# Create your views here.

@login_required
def dashboard(request):
    return render(request, "dashboard/profile.html")

@login_required
def offer(request):
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            new_offer = RideOffer.objects.create(
                driver = request.user,
                vehicle_type = request.POST["vehicle_type"],
                location = request.POST["location"],
                begin_date = request.POST["begin_date"],
                end_date = request.POST["end_date"],
                pricing_model = request.POST["pricing_model"],
                price = request.POST["price"],
                max_load = request.POST["max_load"],
                size = request.POST["size"],
                description = request.POST["descrition"]
            )
            new_offer.save
    
    form = OfferForm()
    return render(request, "dashboard/offer.html", {"form": form})

@login_required
def rent(request):
    offers = RideOffer.objects.all()
    return render(request, "dashboard/rent.html", {"offers": offers})

@login_required
def request_ride(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = RideRequest.objects.create(
                business = request.user,
                vehicle_type = request.POST["vehicle_type"],
                location = request.POST["location"],
                begin_date = request.POST["begin_date"],
                end_date = request.POST["end_date"],
                pricing_model = request.POST["pricing_model"],
                price = request.POST["price"],
                max_load = request.POST["max_load"],
                size = request.POST["size"],
                description = request.POST["descrition"]
            )

    return render(request, "dashboard/request.html")

@login_required
def contract(request):
    requests = RideRequest.objects.all()
    return render(request, "dashboard/contract.html", {"requests": requests})

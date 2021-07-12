from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OfferForm, RequestForm
from .models import RideOffer, RideRequest

# Create your views here.

@login_required
def dashboard(request):
    offers = RideOffer.objects.all()
    requests = RideRequest.objects.all()

    your_offers = [o for o in offers if o.driver == request.user]
    your_requests = [r for r in requests if r.business == request.user]

    return render(request, "dashboard/profile.html", {"offers": your_offers, "requests": your_requests})

@login_required
def offer(request):
    print("passed")
    if request.method == "POST":
        """
        print("passed2")
        form = OfferForm(request.POST)
        if form.is_valid():
            print("passed3")"""
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
            description = request.POST["description"]
        )
        new_offer.save()
    
    form = OfferForm()
    return render(request, "dashboard/makeoffer.html", {"form": form})

@login_required
def rent(request):
    offers = RideOffer.objects.all()
    offers = [offer for offer in offers if not offer.reserved]

    return render(request, "dashboard/rent.html", {"offers": offers})

@login_required
def offer_details(request, **kwargs):
    offer_name = kwargs.get("offer_name")
    offer = RideOffer.objects.get(pk=offer_name)

    return render(request, "dashboard/offer.html", {"offer": offer})

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
            new_request.save()

    form = RequestForm()
    return render(request, "dashboard/makerequest.html", {"form": form})

@login_required
def contract(request):
    requests = RideRequest.objects.all()
    requests = [request for request in requests if not request.reserved]

    return render(request, "dashboard/contractlist.html", {"requests": requests})

@login_required
def contract_details(request, **kwargs):
    contract_name = kwargs.get("contract_name")
    contract = RideOffer.objects.get(pk=contract_name)

    return render(request, "dashboard/contract.html", {"contract": contract})

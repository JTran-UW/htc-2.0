from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OfferForm

# Create your views here.

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def offer(request):
    if request.method == "POST":
        form = OfferForm(request.)
    else:
        return render(request, "dashboard/offer.html")

@login_required
def rent(request):
    return render(request, "dashboard/rent.html")

@login_required
def request_ride(request):
    return render(request, "dashboard/request.html")

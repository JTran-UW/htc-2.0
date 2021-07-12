from django.shortcuts import render, redirect
from .forms import UserAuthenticationForm, RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

# Create your views here.

def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")
    
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                login_user(request, user)
                return redirect("dashboard")
    else:
        form = UserAuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = request.POST["email"]
            password = request.POST["password1"]
            user = authenticate(email=email, password=password)
            
            if user:
                login_user(request, user)
                return redirect("dashboard")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})

def logout(request):
    logout_user(request)
    return redirect("login")

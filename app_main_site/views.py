from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

from django.views.generic import CreateView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

from app_users.forms import RegisterUserForm, LoginUserForm, UpdateProfileForm
from app_users.models import CustomUser


def custom_registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_main_site: home")
    else:
        form = RegisterUserForm()

    return render(request, "registration/registration.html", {"form": form})

def custom_login(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("app_main_site:profile")
    else:
        form = LoginUserForm()
    return render(request, "registration/login.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect('app_main_site:home')

def home(request):
    context = {
        "home": "home page"
    }
    return render(request, "app_main_site/home.html", context)

def profile(request):
    profile = get_object_or_404(CustomUser, pk=request.user.id)
    context = {
        "profile": profile
    }
    return render(request, "app_main_site/profile.html", context)

def update_profile(request):
    current_profile = get_object_or_404(CustomUser, pk=request.user.id)
    if request.method == 'POST':
        updated_form = UpdateProfileForm(request.POST, instance=current_profile)

        if updated_form.is_valid():
            updated_form.save()
            return redirect('app_main_site:profile')
    else:
        updated_form = UpdateProfileForm(instance=current_profile)
        return render(request, "app_main_site/profile.html", {"updated_form": updated_form})
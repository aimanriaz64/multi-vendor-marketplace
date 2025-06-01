from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:dashboard')
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    return render(request, 'accounts/login.html')

def seller_dashboard(request):
    return render(request, 'accounts/seller_dashboard.html')

def customer_dashboard(request):
    return render(request, 'accounts/customer_dashboard.html')

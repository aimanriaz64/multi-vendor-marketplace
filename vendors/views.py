from django.shortcuts import render, redirect
from .forms import VendorProfileForm

def create_profile(request):
    form = VendorProfileForm(request.POST or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('vendors:profile_detail')
    return render(request, 'vendors/profile_form.html', {'form': form})

def profile_detail(request):
    return render(request, 'vendors/profile_detail.html')

from django import forms
from .models import VendorProfile

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['bio', 'experience']

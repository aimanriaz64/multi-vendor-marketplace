from django.db import models
from accounts.models import CustomUser

class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    experience = models.IntegerField()

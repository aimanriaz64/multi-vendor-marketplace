from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

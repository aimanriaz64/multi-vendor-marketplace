from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('profile/create/', views.create_profile, name='profile_create'),
    path('profile/', views.profile_detail, name='profile_detail'),
]

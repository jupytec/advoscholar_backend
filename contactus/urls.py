"""Contact us URL Configuration."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ContactUsView.as_view({"post": "contactus"})),
]

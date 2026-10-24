
from django.urls import path
from myportfolio import views

urlpatterns = [
path("", views.home, name="home"),
path("about_us/", views.about_us, name="about_us"),
path("certificate/", views.certificate, name="certificate"),
path("contact_us/", views.contact, name="contact_us"),
]

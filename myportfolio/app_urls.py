from django.contrib import admin
from django.urls import path

from myportfolio import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home",
    ),

    # Admin
    path(
        "admin/",
        admin.site.urls,
    ),

    # About
    path(
        "about_us/",
        views.about_us,
        name="about_us",
    ),

    # Certificates
    path(
        "certificate/",
        views.certificate,
        name="certificate",
    ),

    # Contact
    path(
        "contact_us/",
        views.contact,
        name="contact_us",
    ),

]
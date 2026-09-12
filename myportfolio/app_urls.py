from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
   path("",views.home,name="home_page"),
   path("about_us/",views.about_us,name="about_us"),
   path("contact_us/",views.contact_us,name="contact_us"),
   path("certificate/",views.certificate,name="certificatepage"),
]
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def home(request):
    return render(request, "html/index.html")


def about_us(request):
    return render(request, "html/about_us.html")


def certificate(request):
    return render(request, "html/certificate.html")


def contact_us(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Database me save
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Gmail par message
        send_mail(
            subject="New Contact Us Message",
            message=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""",
            from_email="tiwarisrijal22@gmail.com",
            recipient_list=["tiwarisrijal22@gmail.com"],
        )

        return redirect("/contact_us/")

    return render(request, "html/contact_us.html")
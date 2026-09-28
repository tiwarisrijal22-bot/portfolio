from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact


def home(request):
    return render(request, "html/index.html")


def about_us(request):
    return render(request, "html/about_us.html")


def certificate(request):
    return render(request, "html/certificate.html")


def contact(request):
    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        # Save message in database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email
        try:
            send_mail(
                "Portfolio Contact Message",
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n\n"
                f"Message:\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:
            print("EMAIL ERROR:", e)

            messages.error(
                request,
                "Message could not be sent. Please try again."
            )

        return redirect("home")

    return render(request, "html/contact_us.html")
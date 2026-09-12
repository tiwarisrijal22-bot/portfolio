from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import resend

from .models import Contact


def home(request):
    return render(request, "html/index.html")


def about_us(request):
    return render(request, "html/about_us.html")


def certificate(request):
    return render(request, "html/certificate.html")


def contact_us(request):
    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        # Save message in database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Send email using Resend
        try:
            resend.api_key = settings.RESEND_API_KEY

            resend.Emails.send({
                "from": "Portfolio <onboarding@resend.dev>",
                "to": [settings.CONTACT_EMAIL],
                "subject": "New Contact Us Message",
                "text": f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""
            })

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:
            print("RESEND EMAIL ERROR:", e)

            messages.warning(
                request,
                "Your message was saved successfully, but email notification could not be sent."
            )

        return redirect("/contact_us/")

    return render(request, "html/contact_us.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Contact
import requests


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

        try:
            # Save contact message to database
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Send email using Resend API
            resend_api_key = settings.RESEND_API_KEY

            if not resend_api_key:
                messages.success(
                    request,
                    "Your message has been saved successfully!"
                )
                return redirect("contact_us")

            email_data = {
                "from": "Portfolio <onboarding@resend.dev>",
                "to": [settings.CONTACT_EMAIL],
                "subject": f"New Portfolio Message from {name}",
                "text": (
                    "New message received from your portfolio.\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Message:\n{message}"
                ),
            }

            response = requests.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {resend_api_key}",
                    "Content-Type": "application/json",
                },
                json=email_data,
                timeout=10,
            )

            if response.status_code in (200, 201):
                messages.success(
                    request,
                    "Your message has been sent successfully!"
                )
            else:
                print("RESEND ERROR:", response.status_code, response.text)

                # DB save successful even if email fails
                messages.success(
                    request,
                    "Your message has been saved successfully!"
                )

        except Exception as e:
            print("CONTACT ERROR:", repr(e))

            # Contact is already saved if this happens after create()
            messages.success(
                request,
                "Your message has been saved successfully!"
            )

        return redirect("contact_us")

    return render(request, "html/contact_us.html")

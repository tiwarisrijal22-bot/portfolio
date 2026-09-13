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


def contact_us(request):
    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        try:
            # Save contact message
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Send email
            send_mail(
                subject=f"New Portfolio Message from {name}",
                message=(
                    "New message received from your portfolio.\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:
            # Print exact error in Render/Vercel logs
            print("CONTACT EMAIL ERROR:", repr(e))

            # Temporarily show exact error on website
            messages.error(
                request,
                f"Email Error: {e}"
            )

        return redirect("contact_us")

    return render(request, "html/contact_us.html")
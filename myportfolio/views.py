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

        # =====================================================
        # SAVE MESSAGE TO DATABASE
        # =====================================================

        try:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )

            database_saved = True

        except Exception as e:
            print("DATABASE ERROR:", repr(e))
            database_saved = False

        # =====================================================
        # SEND EMAIL
        # =====================================================

        try:
            send_mail(
                subject=f"New Portfolio Message from {name}",
                message=(
                    "New message received from your portfolio.\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            email_sent = True

        except Exception as e:
            print("EMAIL ERROR:", repr(e))
            email_sent = False

        # =====================================================
        # FINAL MESSAGE
        # =====================================================

        if database_saved and email_sent:
            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        elif email_sent:
            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        elif database_saved:
            messages.success(
                request,
                "Your message has been saved successfully!"
            )

        else:
            messages.error(
                request,
                "Unable to send your message. Please try again."
            )

        return redirect("contact_us")

    return render(request, "html/contact_us.html")
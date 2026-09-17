from django.shortcuts import render, redirect
from django.contrib import messages
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
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )

            messages.success(
                request,
                "Your message has been saved successfully!"
            )

        except Exception as e:
            print("CONTACT DB ERROR:", repr(e))

            messages.error(
                request,
                "Unable to save your message."
            )

        return redirect("contact_us")

    return render(request, "html/contact_us.html")

from django.shortcuts import render, redirect
from .forms import BookingForm,EditUserForm

from django.shortcuts import get_object_or_404
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User





def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = BookingForm()

    return render(request, "book/booking.html", {"form": form})


def success(request):
    return render(request, "book/success.html")

@login_required
def booking_list(request):
    
    bookings = Booking.objects.all().order_by("-date","-time")
    return render(request, "book/booking_list.html", {"bookings": bookings})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("booking_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required
def approve_booking(request, booking_id):
    if not request.user.is_staff:
        return redirect("booking_list")
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "Approved"
    booking.save()
    return redirect("booking_list")

@login_required
def reject_booking(request, booking_id):
    if not request.user.is_staff:
        return redirect("booking_list")
    
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "Rejected"
    booking.save()
    return redirect("booking_list")

@login_required
def create_booking(request):
   if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # # send confirmation to user
            # send_mail(
            #     subject="Booking Confirmation",
            #     message=f"Hello {booking.name}, your booking for {booking.service} on {booking.date} at {booking.time} was received.",
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[booking.email],
            #     fail_silently=False,
            # )

            # send notification to admin
            # send_mail(
            #     subject="New Booking Submitted",
            #     message=f"A new booking was created by {booking.name} ({booking.email}).",
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=["YOUR_ADMIN_EMAIL@gmail.com"],
            #     fail_silently=False,
            # )
            # email = EmailMessage(
            #     "Booking Confirmation",
            #     f"<h3>Hello {booking.name}</h3><p>Your booking is confirmed.</p>",
            #     settings.EMAIL_HOST_USER,
            #     [booking.email],
            # )
            # email.content_subtype = "html"
            # email.send()
            # messages.success(request, "Your booking was submitted! Check your email.")


            return redirect("booking_list")
                 
   else:
        form = BookingForm()
   return render(request, "book/create_booking.html", {"form": form})

@login_required
def profile(request):
    return render(request, "book/profile.html", {"user": request.user})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditUserForm(instance=request.user)

    return render(request, "book/edit_profile.html", {"form": form})

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-date")
    upcoming = bookings.filter(status="Approved")
    pending = bookings.filter(status="Pending")

    context = {
        "bookings": bookings,
        "upcoming": upcoming[:5],
        "pending": pending[:5],
    }
    
    return render(request, "book/dashboard.html", context)



def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_bookings = Booking.objects.count()
    pending = Booking.objects.filter(status="Pending").count()
    approved = Booking.objects.filter(status="Approved").count()
    rejected = Booking.objects.filter(status="Rejected").count()
    total_users = User.objects.count()

    # Most popular service
    from django.db.models import Count
    service_stats = Booking.objects.values('service').annotate(count=Count('service')).order_by('-count')

    context = {
        "total_bookings": total_bookings,
        "pending": pending,
        "approved": approved,
        "rejected": rejected,
        "total_users": total_users,
        "service_stats": service_stats,
    }

    return render(request, "book/admin_dashboard.html", context)

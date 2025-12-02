from django import forms
from .models import Booking
    
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "phone", "service", "date", "time", "guests", "notes"]
        labels = {
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "service": "Service Type",
            "date": "Preferred Date",
            "time": "Preferred Time",
            "guests": "Number of Attendees",
            "notes": "Additional Notes",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "example@mail.com"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+254700000000"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "guests": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "placeholder": "Optional message", "rows": 3}),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

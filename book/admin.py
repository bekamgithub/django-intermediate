from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "service", "date", "time", "status")
    list_filter = ("service", "status", "date")
    search_fields = ("name", "email", "phone")
    ordering = ("date", "time")
    list_per_page = 20

admin.site.register(Booking, BookingAdmin)

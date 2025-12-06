from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('success/', views.success, name='success'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('', views.register, name="register"),
    path('booking/<int:booking_id>/approve/', views.approve_booking, name="approve_booking"),
    path('booking/<int:booking_id>/reject/', views.reject_booking, name="reject_booking"),
    path("booking/new/", views.create_booking, name="create_booking"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),



]
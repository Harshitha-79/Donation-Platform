from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_donation, name='add_donation'),
    path('donations/', views.donation_list, name='donation_list'),
    path('edit/<int:id>/', views.edit_donation, name='edit_donation'),
    path('delete/<int:id>/', views.delete_donation, name='delete_donation'),
    path('claim/<int:id>/', views.mark_claimed, name='claim'),  # For home.html
]

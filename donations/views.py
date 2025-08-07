from django.shortcuts import render, redirect, get_object_or_404
from .models import Donation
from .forms import DonationForm

def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    donations = Donation.objects.all()
    if query:
        donations = donations.filter(title__icontains=query)
    if category:
        donations = donations.filter(category=category)

    return render(request, 'home.html', {'donations': donations, 'query': query})

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donation_list.html', {'donations': donations})

def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'add.html', {'form': form})

def edit_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'add.html', {'form': form})

def delete_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect('donation_list')

def mark_claimed(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.is_claimed = True
    donation.save()
    return redirect('home')

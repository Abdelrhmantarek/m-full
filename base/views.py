from django.shortcuts import render

# Create your views here.

# HOME-PAGE
def home(request):
    return render(request, 'index.html')

# MENU-PAGE
def menu(request):
    return render(request, 'menu.html')


# RESERVATION-PAGE
def reservation(request):
    return render(request, 'reservation.html')


# CONTACT-PAGE
def contact(request):
    return render(request, 'contact.html')

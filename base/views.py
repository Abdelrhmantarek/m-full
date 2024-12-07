from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.

# HOME-PAGE
def home(request):
    return render(request, 'index.html')


# Handle AJAX Contact Form Submission
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact form data to the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        return JsonResponse({'success': True, 'message': 'Your message has been sent!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request.'}, status=400)

# MENU-PAGE
def menu(request):
    return render(request, 'menu.html')


# RESERVATION-PAGE
def reservation(request):
    return render(request, 'reservation.html')


def submit_reservation(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            seats = request.POST.get('seats')
            special_requests = request.POST.get('special_requests', '')

            # Save the reservation data
            Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                seats=seats,
                special_requests=special_requests
            )
            return JsonResponse({"message": "Reservation submitted successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": "Failed to submit reservation. " + str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)


# CONTACT-PAGE
def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render  # Import render to render templates with context data.
from django.http import JsonResponse  # Import JsonResponse to send JSON responses for AJAX requests.
from .models import *  # Import all models from the current app.
# API IMPORTS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.

# HOME-PAGE
def home(request):
    """
    Renders the homepage with categorized menu items.
    """
    # Fetch categorized menu items from the database.
    starters = Menu.objects.filter(type="Starter")  # Fetch all starters.
    main_courses = Menu.objects.filter(type="Main Course")  # Fetch all main courses.
    soups = Menu.objects.filter(type="Soup")  # Fetch all soups.
    desserts = Menu.objects.filter(type="Dessert")  # Fetch all desserts.

    print(starters)  # Debugging: Print the starters to the console.

    # Define the context to pass data to the template.
    context = {
        "starters": starters,
        "main_courses": main_courses,
        "soups": soups,
        "desserts": desserts
    }

    # Render the 'index.html' template with the context data.
    return render(request, 'index.html', context)


# Handle AJAX Contact Form Submission
def submit_contact(request):
    """
    Handles the submission of the contact form via AJAX.
    """
    if request.method == 'POST':  # Ensure the request method is POST.
        # Retrieve form data from the POST request.
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact form data to the database.
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Send a success response as JSON.
        return JsonResponse({'success': True, 'message': 'Your message has been sent!'})
    else:
        # Send an error response for invalid requests.
        return JsonResponse({'success': False, 'message': 'Invalid request.'}, status=400)


# MENU-PAGE
def menu(request):
    """
    Renders the menu page with all menu items grouped by type.
    """
    # Fetch all menu items from the database and order them by type.
    menu_items = Menu.objects.all().order_by('type')  # Optional: customize the ordering.
    
    # Render the 'menu.html' template with the menu items.
    return render(request, 'menu.html', {'menu_items': menu_items})


# RESERVATION-PAGE
def reservation(request):
    """
    Renders the reservation page.
    """
    return render(request, 'reservation.html')


# Handle Reservation Form Submission
def submit_reservation(request):
    """
    Handles the submission of the reservation form via AJAX.
    """
    if request.method == "POST":  # Ensure the request method is POST.
        try:
            # Retrieve form data from the POST request.
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            seats = request.POST.get('seats')
            special_requests = request.POST.get('special_requests', '')  # Optional field.

            # Save the reservation data to the database.
            Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                seats=seats,
                special_requests=special_requests
            )
            # Send a success response as JSON.
            return JsonResponse({"message": "Reservation submitted successfully!"}, status=200)
        except Exception as e:
            # Send an error response with the exception message.
            return JsonResponse({"error": "Failed to submit reservation. " + str(e)}, status=500)
    else:
        # Send an error response for invalid request methods.
        return JsonResponse({"error": "Invalid request method."}, status=400)


# CONTACT-PAGE
def contact(request):
    """
    Renders the contact page.
    """
    return render(request, 'contact.html')




############## API CREATION ############## 
class MenuListView(APIView):
    """
    API View to list all menu items in the restaurant.
    """
    def get(self, request, *args, **kwargs):
        menu_items = Menu.objects.all()  # Get all the menu items from the database
        serializer = MenuSerializer(menu_items, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)

############## API CREATION ############## 


from django.urls import path  # Import Django's path function to define URL patterns.
from . import views  # Import the views module from the current app.

# Define URL patterns for the app.
urlpatterns = [
    path('', views.home, name="home"),  
    # The root URL ('') routes to the `home` view. 
    # The `name` parameter assigns a name to this URL for reverse URL resolution.

    path('menu/', views.menu, name="menu"),  
    # The 'menu/' URL routes to the `menu` view, displaying the restaurant's menu page.

    path('reservation/', views.reservation, name="reservation"),  
    # The 'reservation/' URL routes to the `reservation` view, handling reservation requests.

    path('contact/', views.contact, name="contact"),  
    # The 'contact/' URL routes to the `contact` view, displaying the contact form.

    path('submit-contact/', views.submit_contact, name='submit_contact'),  
    # The 'submit-contact/' URL routes to the `submit_contact` view, 
    # handling form submissions for the contact page.

    path('submit-reservation/', views.submit_reservation, name='submit_reservation'),  
    # The 'submit-reservation/' URL routes to the `submit_reservation` view, 
    # handling form submissions for reservations.

    # API endpoint for listing menu items
    path('api/menu/', views.MenuListView.as_view(), name='api_menu_list'),  # Adding the API endpoint

]

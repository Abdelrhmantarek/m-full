from django.contrib import admin  # Import the admin module from Django to customize the admin interface.
from .models import *  # Import all models from the current app's models file.

# Customize the admin site's header, title, and index title.
# This helps personalize the admin interface for the app.
admin.site.site_header = "Manolya Dashboard"  # Sets the header of the admin interface.
admin.site.site_title = "Manolya Dashboard"  # Sets the title of the admin site in the browser tab.
admin.site.index_title = "Manolya App"  # Sets the title on the admin dashboard index page.

# Register your models here.
# This makes the models accessible and manageable via the Django admin interface.
admin.site.register(Contact)  # Registers the Contact model to the admin interface.
admin.site.register(Reservation)  # Registers the Reservation model to the admin interface.
admin.site.register(Menu)  # Registers the Menu model to the admin interface.

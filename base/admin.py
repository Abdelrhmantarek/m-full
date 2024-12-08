from django.contrib import admin
from .models import *

# Customize the admin site's title
admin.site.site_header = "Manolya Dashboard"
admin.site.site_title = "Manolya Dashboard"
admin.site.index_title = "Manolya App"


# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Menu)

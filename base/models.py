from django.db import models  # Import Django's models module to define database models.

# Create your models here.

# Contact Model: Stores contact form submissions from users.
class Contact(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Full Name"
    )  # A text field for the user's full name with a maximum length of 255 characters.
    email = models.EmailField(
        verbose_name="Email Address"
    )  # A field for storing valid email addresses.
    subject = models.CharField(
        max_length=255, verbose_name="Subject"
    )  # A text field for the subject of the message.
    message = models.TextField(
        verbose_name="Message"
    )  # A text field for the body of the message, no length limit.

    def __str__(self):
        # Represents the object as a string, combining the name and subject fields.
        return f"{self.name} - {self.subject}"

    class Meta:
        # Meta options for the model.
        verbose_name = "Contact"  # Singular name displayed in the admin panel.
        verbose_name_plural = "Contacts"  # Plural name displayed in the admin panel.


# Reservation Model: Represents a reservation made by a user.
class Reservation(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Full Name"
    )  # A text field for the user's full name.
    email = models.EmailField(
        verbose_name="Email Address"
    )  # A field for the user's email address.
    phone = models.CharField(
        max_length=15, verbose_name="Phone Number"
    )  # A text field for the user's phone number.
    date = models.DateField(
        verbose_name="Reservation Date"
    )  # A date field for the reservation.
    time = models.TimeField(
        verbose_name="Reservation Time"
    )  # A time field for the reservation.
    seats = models.PositiveIntegerField(
        verbose_name="Number of Seats"
    )  # A positive integer field for the number of seats reserved.
    special_requests = models.TextField(
        blank=True,
        null=True,
        verbose_name="Special Requests",
    )  # An optional text field for any special requests.

    def __str__(self):
        # Represents the object as a string, combining the name, date, and time.
        return f"Reservation for {self.name} on {self.date} at {self.time}"

    class Meta:
        # Meta options for the model.
        verbose_name = "Reservation"  # Singular name displayed in the admin panel.
        verbose_name_plural = "Reservations"  # Plural name displayed in the admin panel.


# Menu Model: Represents a menu item in the restaurant.
class Menu(models.Model):
    TYPE_CHOICES = [
        ("Starter", "Starter"),
        ("Main Course", "Main Course"),
        ("Soup", "Soup"),
        ("Dessert", "Dessert"),
    ]  # Defines the types of menu items as choices.

    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, verbose_name="Menu Type"
    )  # A field for the menu type, restricted to the predefined choices.
    name = models.CharField(
        max_length=255, verbose_name="Menu Item Name"
    )  # A text field for the name of the menu item.
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price"
    )  # A decimal field for the price, supporting up to 10 digits with 2 decimal places.
    image = models.ImageField(
        upload_to="menu_images/",
        blank=True,
        null=True,
        verbose_name="Image",
    )  # An optional image field for the menu item, storing images in the "menu_images/" directory.

    def __str__(self):
        # Represents the object as a string, combining the name, type, and price.
        return f"{self.name} ({self.type}) - ${self.price:.2f}"

    class Meta:
        # Meta options for the model.
        verbose_name = "Menu"  # Singular name displayed in the admin panel.
        verbose_name_plural = "Menus"  # Plural name displayed in the admin panel.

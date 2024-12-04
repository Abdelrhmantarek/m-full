from django.db import models

# Create your models here.

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Reservation Model
class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    date = models.DateField(verbose_name="Reservation Date")
    time = models.TimeField(verbose_name="Reservation Time")
    seats = models.PositiveIntegerField(verbose_name="Number of Seats")
    special_requests = models.TextField(blank=True, null=True, verbose_name="Special Requests")

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


# Menu Model
class Menu(models.Model):
    TYPE_CHOICES = [
        ("Starter", "Starter"),
        ("Main Course", "Main Course"),
        ("Soup", "Soup"),
        ("Dessert", "Dessert"),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Menu Type")
    name = models.CharField(max_length=255, verbose_name="Menu Item Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price:.2f}"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


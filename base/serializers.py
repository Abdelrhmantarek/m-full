from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'type', 'name', 'price', 'image']  # Define the fields to include in the API response

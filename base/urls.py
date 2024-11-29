from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('reservation/', views.reservation, name="reservation"),
    path('contact/', views.contact, name="contact")
]



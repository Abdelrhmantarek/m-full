from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('reservation/', views.reservation, name="reservation"),
    path('contact/', views.contact, name="contact"),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('submit-reservation/', views.submit_reservation, name='submit_reservation'),
]



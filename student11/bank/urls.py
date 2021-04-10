from django.contrib import admin
from django.urls import path
from bank import views
urlpatterns = [
    path('', views.bank,name='bank'),
    path('contactus', views.contactus,name='contactus'),
    path('contact', views.contact1,name='contact'),
]

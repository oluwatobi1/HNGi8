from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact_details, name='contact_details'),
    path('sent', views.index, name='index'),
]
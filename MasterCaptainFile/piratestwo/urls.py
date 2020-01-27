from django.urls import path, include
from . import views

urlpatterns = [
    path("items/", views.item_location),
    path("map/", views.map),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path("items/", views.get_items),
    path("map/", views.map),
    
]

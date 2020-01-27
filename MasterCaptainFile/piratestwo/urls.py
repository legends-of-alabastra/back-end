from django.urls import path, include
from . import views
# don't forget to add /api/ to the front of the below endpoints

urlpatterns = [
    path("items/", views.item_location),
    path("map/", views.map),
    path("merchant/", views.merchant_weapons),
    path("bigbang/", views.bigbang),
    path("getItems/", views.get_items)
]
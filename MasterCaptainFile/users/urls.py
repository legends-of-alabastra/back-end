from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from . import views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LoginView.as_view(), name= 'knox_logout'),
    path("playeritems/", views.player_items),
    path("additems/", views.add_items),
    path("getitems/", views.pusher_item_locations),
    path("playerinventory/", views.player_inventory)

    # path('api/auth/logins', views.my_view),
]

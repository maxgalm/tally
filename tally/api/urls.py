from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# api/
urlpatterns = [
    path("auth/", obtain_auth_token ),
    path("drinks/", include("drinks.urls")),
    path("items/", include("items.urls")),
]
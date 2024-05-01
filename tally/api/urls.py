from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# api/
urlpatterns = [
    path("auth/", obtain_auth_token ),
    path("persons/", views.PersonListCreate.as_view()),
    path("persons/<int:pk>/", views.PersonRetrieveUpdateDestroy.as_view()),
    path("drinks/", include("drinks.urls")),
    path("items/", include("items.urls")),
]
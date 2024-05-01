from django.urls import path, include
from . import views

# api/
urlpatterns = [
    path("persons/", views.PersonListCreate.as_view()),
    path("persons/<int:pk>/", views.PersonRetrieveUpdateDestroy.as_view()),
    path("drinks/", include("drinks.urls")),
    path("items/", include("items.urls")),
]
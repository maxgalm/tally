from django.urls import path
from . import views

# api/drinks/
urlpatterns = [
    path("", views.DrinkListCreate.as_view(), name="drinks-list"),
    path("<int:pk>/", views.DrinkRetrieveUpdateDestroy.as_view(), name="drinks-detail"),
]
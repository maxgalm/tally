from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.PersonListCreate.as_view(), name="person-view"),
    path("drinks/", views.DrinkListCreate.as_view(), name="drink-view"),
    path("tally/", views.TallyListCreate.as_view(), name="tally-view"),
]
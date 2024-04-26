from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.PersonListCreate.as_view(), name="person-view"),
    path("persons/<int:pk>/", views.PersonRetrieveUpdateDestroy.as_view(), name="person-view-single"),
    path("drinks/", views.DrinkListCreate.as_view(), name="drink-view"),
    path("drinks/<int:pk>/", views.DrinkRetrieveUpdateDestroy.as_view(), name="drink-view-single"),
    path("tally/", views.TallyListCreate.as_view(), name="tally-view"),
    path("tally/<int:pk>/", views.TallyRetrieveUpdateDestroy.as_view(), name="tally-view-single"),
]
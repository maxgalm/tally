from django.urls import path
from . import views

urlpatterns = [
    path("", views.DrinkListCreate.as_view()),
    path("<int:pk>/", views.DrinkRetrieveUpdateDestroy.as_view()),
]
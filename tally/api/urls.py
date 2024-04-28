from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.PersonListCreate.as_view()),
    path("persons/<int:pk>/", views.PersonRetrieveUpdateDestroy.as_view()),
    path("drinks/", views.DrinkListCreate.as_view()),
    path("drinks/<int:pk>/", views.DrinkRetrieveUpdateDestroy.as_view()),
    path("tally/", views.TallyListCreate.as_view()),
    path("tally/<int:pk>/update/", views.TallyUpdateAPIView.as_view()),
    path("tally/<int:pk>/delete/", views.TallyDestroyAPIView.as_view()),
    path("tally/<int:pk>/", views.TallyDetailAPIView.as_view())
]
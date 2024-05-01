from django.urls import path
from . import views

urlpatterns = [
    path("", views.TallyListCreate.as_view()),
    path("<int:pk>/", views.TallyDetailAPIView.as_view()),
    path("<int:pk>/update/", views.TallyUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.TallyDestroyAPIView.as_view())
]
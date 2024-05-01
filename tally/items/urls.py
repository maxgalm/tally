from django.urls import path
from . import views

urlpatterns = [
    path("", views.TallyItemListCreate.as_view()),
    path("<int:pk>/", views.TallyItemDetailAPIView.as_view()),
    path("<int:pk>/update/", views.TallyItemUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.TallyItemDestroyAPIView.as_view())
]
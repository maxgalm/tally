from django.urls import path
from . import views

# api/items/
urlpatterns = [
    path("", views.TallyItemListCreateAPIView.as_view(), name="items-list"),
    path("<int:pk>/", views.TallyItemDetailAPIView.as_view(), name="items-detail"),
    path("<int:pk>/update/", views.TallyItemUpdateAPIView.as_view(), name="items-update"),
    path("<int:pk>/delete/", views.TallyItemDestroyAPIView.as_view(), name="items-delete")
]
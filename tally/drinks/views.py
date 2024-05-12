from rest_framework import generics

from .models import Drink
from .serializers import DrinkSerializer, DrinkDetailSerializer
from api.mixins import DrinkEditorPermissionMixin, DrinkQuerySetMixin

# Create your views here.
class DrinkListCreate(
    DrinkEditorPermissionMixin,
    DrinkQuerySetMixin,
    generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    allow_staff_view = True

class DrinkRetrieveUpdateDestroy(
    DrinkEditorPermissionMixin,
    DrinkQuerySetMixin,
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkDetailSerializer
    allow_staff_view = True
    lookup_field = "pk"
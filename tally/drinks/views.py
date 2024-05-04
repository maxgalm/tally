from rest_framework import generics

from .models import Drink
from .serializers import DrinkSerializer
from api.mixins import DrinkEditorPermissionMixin

# Create your views here.
class DrinkListCreate(
    DrinkEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieveUpdateDestroy(
    DrinkEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = "pk"
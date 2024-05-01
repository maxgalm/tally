from .models import Drink
from .serializers import DrinkSerializer

from rest_framework import generics

# Create your views here.
class DrinkListCreate(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = "pk"
from rest_framework import generics, authentication, permissions

from .models import Drink
from .serializers import DrinkSerializer
from .permissions import IsDrinkEditorPermission

# Create your views here.
class DrinkListCreate(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsDrinkEditorPermission]

class DrinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsDrinkEditorPermission]
    lookup_field = "pk"
from .models import Person, Drink, Tally
from .serializers import PersonSerializer, DrinkSerializer, TallySerializer, NestedTallySerializer

from rest_framework import generics

##PERSON

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = "pk"

##DRINK

class DrinkListCreate(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = "pk"

##TALLY

class TallyListCreate(generics.ListCreateAPIView):
    queryset = Tally.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NestedTallySerializer
        return TallySerializer

class TallyDetailAPIView(generics.RetrieveAPIView):
    queryset = Tally.objects.all()
    serializer_class = NestedTallySerializer

class TallyUpdateAPIView(generics.UpdateAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer
    lookup_field = "pk"

class TallyDestroyAPIView(generics.DestroyAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer
    lookup_field = "pk"
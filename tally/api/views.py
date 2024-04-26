from django.shortcuts import render
from rest_framework import generics
from .models import Person, Drink, Tally
from .serializers import PersonSerializer, DrinkSerializer, TallySerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = "pk"

class DrinkListCreate(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = "pk"

class TallyListCreate(generics.ListCreateAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer

class TallyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer
    lookup_field = "pk"
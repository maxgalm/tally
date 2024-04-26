from django.shortcuts import render
from rest_framework import generics
from .models import Person, Drink, Tally
from .serializers import PersonSerializer, DrinkSerializer, TallySerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DrinkListCreate(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class TallyListCreate(generics.ListCreateAPIView):
    queryset = Tally.objects.all()
    serializer_class = TallySerializer
from rest_framework import serializers
from .models import Person, Drink, Tally

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "date_joined"]

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ["id", "name", "description", "price"]

class TallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tally
        fields = ["id", "person", "drink", "created_at"]

class NestedTallySerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    drink = DrinkSerializer(read_only=True)

    class Meta:
        model = Tally
        fields = ["id", "person", "drink", "created_at"]
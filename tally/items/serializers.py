from .models import TallyItem
from drinks.serializers import DrinkSerializer

from rest_framework import serializers

class TallyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TallyItem
        fields = ["id", "user", "drink", "created_at"]

class NestedTallyItemSerializer(serializers.ModelSerializer):
    # person = PersonSerializer(read_only=True)
    drink = DrinkSerializer(read_only=True)

    class Meta:
        model = TallyItem
        fields = ["id", "user", "drink", "created_at"]
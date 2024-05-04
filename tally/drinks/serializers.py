from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="drinks-detail",
        lookup_field="pk"
    )
    class Meta:
        model = Drink
        fields = [
            "id",
            "url",
            "name",
            "description",
            "price"
        ]

class DrinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = [
            "id",
            "name",
            "description",
            "price"
        ]
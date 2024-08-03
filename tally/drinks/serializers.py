from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="drinks-detail",
        lookup_field="pk"
    )
    currency = serializers.CharField(read_only=True)
    public = serializers.BooleanField(read_only=True)
    class Meta:
        model = Drink
        fields = [
            "id",
            "url",
            "name",
            "description",
            "price",
            "currency",
            "public"
        ]

class DrinkDetailSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(read_only=True)
    public = serializers.BooleanField(read_only=True)
    class Meta:
        model = Drink
        fields = [
            "id",
            "name",
            "description",
            "price",
            "currency",
            "public",
        ]
from rest_framework import serializers

from .models import TallyItem
from drinks.serializers import DrinkSerializer
from api.serializers import UserPublicSerializer

class TallyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TallyItem
        fields = [
            "id",
            "debtor",
            "drink",
            "created_at"
        ]

class NestedTallyItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="items-detail",
        lookup_field="pk"
    )
    debtor = UserPublicSerializer(read_only=True)
    drink = DrinkSerializer(read_only=True)
    created_by = UserPublicSerializer(read_only=True)

    class Meta:
        model = TallyItem
        fields = [
            "id",
            "url",
            "debtor",
            "drink",
            "created_at",
            "created_by"
        ]
from .models import TallyItem
from .serializers import TallyItemSerializer, NestedTallyItemSerializer

from rest_framework import generics
from api.mixins import UserQuerySetMixin

# Create your views here.
class TallyItemListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView):
    queryset = TallyItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NestedTallyItemSerializer
        return TallyItemSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TallyItemDetailAPIView(
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = NestedTallyItemSerializer

class TallyItemUpdateAPIView(
    UserQuerySetMixin,
    generics.UpdateAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = TallyItemSerializer
    lookup_field = "pk"

class TallyItemDestroyAPIView(
    UserQuerySetMixin,
    generics.DestroyAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = TallyItemSerializer
    lookup_field = "pk"
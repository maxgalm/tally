from .models import TallyItem
from .serializers import TallyItemSerializer, NestedTallyItemSerializer

from rest_framework import generics

# Create your views here.
class TallyItemListCreate(generics.ListCreateAPIView):
    queryset = TallyItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NestedTallyItemSerializer
        return TallyItemSerializer

class TallyItemDetailAPIView(generics.RetrieveAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = NestedTallyItemSerializer

class TallyItemUpdateAPIView(generics.UpdateAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = TallyItemSerializer
    lookup_field = "pk"

class TallyItemDestroyAPIView(generics.DestroyAPIView):
    queryset = TallyItem.objects.all()
    serializer_class = TallyItemSerializer
    lookup_field = "pk"
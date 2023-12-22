from rest_framework import generics
from .models import Property, PropertyImage
from .serializers import PropertySerializer

class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Property
    lookup_field = 'slug'
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
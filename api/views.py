from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList

from django.shortcuts import render

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
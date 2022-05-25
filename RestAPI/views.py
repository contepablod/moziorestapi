from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProviderSerializer, ServiceAreaSerializer
from .models import Provider, ServiceArea


# Create your views here.

class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

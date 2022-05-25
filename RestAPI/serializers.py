from rest_framework import serializers
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['Name', 'Email', 'Phone', 'Language', 'Currency']


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['Name', 'Price', 'Location']

from .models import Country, Shipment
from rest_framework import viewsets, permissions
from .serializers import CountrySerializer, ShipmentSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountrySerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ShipmentSerializer

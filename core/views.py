from django.shortcuts import render
from core.models import Cliente, Direccion, Imagen
from core.serializers import ClienteSerializer, DireccionSerializer, ImagenSerializer, PosicionSerializer
from rest_framework import viewsets


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().prefetch_related('direcciones')
    serializer_class = ClienteSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all().prefetch_related('imagenes')
    serializer_class = DireccionSerializer


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = PosicionSerializer

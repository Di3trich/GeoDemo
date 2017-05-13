from rest_framework import serializers
from core.models import Cliente, Direccion, Imagen


class DireccionLightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ('url', 'direccion', 'principal', 'latitud', 'longitud')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    direcciones = DireccionLightSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ('url', 'nombres', 'apellidos', 'documento', 'direcciones')


class ImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imagen
        fields = ('url', 'descripcion', 'imagen', 'direccion')


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    imagenes = ImagenSerializer(many=True, read_only=True)

    class Meta:
        model = Direccion
        fields = ('url', 'direccion', 'principal', 'latitud', 'longitud', 'cliente', 'imagenes')


class PosicionSerializer(serializers.HyperlinkedModelSerializer):
    #url =

    class Meta:
        model = Direccion
        fields = ('direccion', 'latitud', 'longitud', 'principal', 'cliente')

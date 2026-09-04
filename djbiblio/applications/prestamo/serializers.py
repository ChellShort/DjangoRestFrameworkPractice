from rest_framework import serializers
from .models import Devolucion, Prestamo

class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Devolucion
        fields = (
            'prestamo',
            'fecha'
        ) # o tambien puedes usar ('__all__')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('__all__')
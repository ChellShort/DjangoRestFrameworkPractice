from rest_framework import serializers
from .models import Autor, Libro
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Autor
        fields = (
            'nombres',
            'apellidos',
            'nacionalidad'
        ) # o tambien puedes usar ('__all__')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = (
            'titulo', 
            'autor', 
            'lanzamiento'
            )
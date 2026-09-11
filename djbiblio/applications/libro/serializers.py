from rest_framework import serializers, pagination
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
        
class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 50
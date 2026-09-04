from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from applications.libro.models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer

class lista_autores(ListAPIView):
    # queryset = Autor.objects.all() # Esto se transforma en sintaxis SQL
    serializer_class = AutorSerializer

    def get(self, request, *args, **kwargs): # Esto sera lo que se obtenga por encima de cualquier otra función, es por eso que parece el resultado de esta función por sobre get_queryset
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        # query_set = Autor.objects.all() -> Select * from Autor
        query_set = Autor.objects.listar_autores_nacionalidad('Mexicana')
        return query_set
    
class FiltraAutores(ListAPIView):
    serializer_class = AutorSerializer

    def get_queryset(self):
        nacionalidad = self.kwargs["nacionalidad"]
        print(f"Buscando nacionalidad: {nacionalidad}")
        query_set = Autor.objects.listar_autores_nacionalidad(nacionalidad)
        return query_set
    
class FiltraPorNumero(ListAPIView):
    serializer_class= AutorSerializer
    
    def get_queryset(self):
        pais = self.kwargs["pais"]
        print(f"Buscando pais: {pais}")
        query_set = Autor.objects.listar_autores_nacionalidad("Mexicana")
        return query_set
    
class ListarLibrosPosteriores(ListAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        year = self.kwargs["year"]
        query_set = Libro.objects.listar_libros_posteriores_año(year)
        return query_set
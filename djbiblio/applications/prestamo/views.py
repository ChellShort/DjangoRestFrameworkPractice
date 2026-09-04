from django.shortcuts import render
from rest_framework.generics import ListAPIView # Hats ahora lo unico que ocupamos de DjangoRestFramework
from .serializers import DevolucionSerializer, PrestamoSerializer
from .models import Devolucion, Prestamo

# Create your views here.
class lista_devoluciones(ListAPIView):
    serializer_class = DevolucionSerializer
    
    def get_queryset(self):
        query_set = Devolucion.objects.listar_devoluciones_all()
        return query_set
    
class lista_prestamos(ListAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        query_set = Prestamo.objects.listar_prestamos_all()
        return query_set
    
class lista_prestamos_fecha(ListAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        query_set = Prestamo.objects.listar_prestamos_fecha('2026-09-03', 2)
        return query_set
from django.db import models
from applications.libro.models import Libro
from .managers import DevolucionManager, PrestamoManager

class Estudiante(models.Model):
    DNI = models.CharField('DNI', max_length=50)
    nombres = models.CharField('nombres', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

# Create your models here.
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name = "Libro")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name = "Estudiante")
    descripcion = models.CharField('descripcion', max_length=50, blank=True)
    fecha = models.DateField('fecha')
    
    objects = PrestamoManager()
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return f'{self.libro} -> {self.estudiante}'

class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, verbose_name = "Prestamo")
    fecha = models.DateField('fecha')
    
    objects = DevolucionManager()
    
    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'
        
    def __str__(self):
        return f'{self.prestamo} ({self.fecha})'
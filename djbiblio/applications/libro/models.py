from django.db import models
from .managers import AutorManager, LibroManager

# Las entidades de la DB
class Autor(models.Model):
    nombres = models.CharField('nombre', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    nacionalidad = models.CharField('nacionalidad', max_length=50)
    
    objects = AutorManager()
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Editorial(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    
    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
            
    def __str__(self):
        return self.nombre

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField('titulo', max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, verbose_name = "Editorial")
    lanzamiento = models.DateField('lanzamiento')
    portada = models.ImageField('portada', upload_to='libro', blank=True, null=True)
    
    objects = LibroManager()
    
    class Meta:
            verbose_name = 'Libro'
            verbose_name_plural = 'Libros'
            
    def __str__(self):
        return f"{self.titulo} ({self.autor}) {self.lanzamiento.year}"
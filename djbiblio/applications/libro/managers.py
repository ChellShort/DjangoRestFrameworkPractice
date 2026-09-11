from django.db import models

# Los managers! nos sirven para aplicar filtros yu en general consultas a base de datos
class AutorManager(models.Manager):
    def listar_autores_nacionalidad(self, nacionalidad:str):
        return self.filter(
            nacionalidad= nacionalidad
        )
        
class LibroManager(models.Manager):
    def listar_libros_posteriores_año(self, año:str):
        año = año # ?
        return self.filter(
            lanzamiento__year__gt = año
        )
        
    def libros_por_titulo(self, titulo):
        titulo = titulo
        return self.filter(
            titulo__icontains = titulo
        ).order_by('titulo')
        
    def filtrar_libros(self, titulo, año):
        titulo = titulo
        año = año
        return self.filter(
            titulo__icontains = titulo,
            lanzamiento__year__gt = año
        )
        
    def filtrar_libros_por_autor(self, autor):
        autor = autor
        return self.filter(
            autor__nombres__icontains = autor
        ).order_by('lanzamiento')
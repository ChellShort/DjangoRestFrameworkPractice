from django.db import models

# Los managers! nos sirven para aplicar filtros yu en general consultas a base de datos
class AutorManager(models.Manager):
    def listar_autores_nacionalidad(self, nacionalidad:str):
        return self.filter(
            nacionalidad= nacionalidad
        )
        
class LibroManager(models.Manager):
    def listar_libros_posteriores_año(self, año:str):
        año = año#?
        return self.filter(
            lanzamiento__year__gt = año
        )
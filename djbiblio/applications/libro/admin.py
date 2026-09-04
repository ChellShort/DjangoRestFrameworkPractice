from django.contrib import admin
from applications.libro.models import Autor, Editorial, Libro


# Register your models here.

@admin.register(Autor)
class admin_autor(admin.ModelAdmin):
    list_display = (
        "nombres",
        "apellidos",
        "nacionalidad"
    )
    
@admin.register(Editorial)
class admin_editorial(admin.ModelAdmin):
    list_display = (
        "nombre",
    )

@admin.register(Libro) # Equivalente a admin.site.register(Libro, admin_libro) despues de definir la clase
class admin_libro(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "editorial",
        "lanzamiento",
        "portada"
    )
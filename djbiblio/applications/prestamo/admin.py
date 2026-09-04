from django.contrib import admin
from applications.prestamo.models import Estudiante
from applications.prestamo.models import Estudiante, Prestamo, Devolucion

# Register your models here.

# admin.site.register(Estudiante)
@admin.register(Prestamo)
class admin_prestamo(admin.ModelAdmin):
    list_display = (
        "libro",
        "estudiante",
        "descripcion",
        "fecha"
    )

@admin.register(Devolucion)
class admin_devolucion(admin.ModelAdmin):
    list_display = (
        "prestamo",
        "fecha"
    )

@admin.register(Estudiante)
class admin_author(admin.ModelAdmin):
    list_display = (
        "DNI",
        "nombres",
        "apellidos"
    )
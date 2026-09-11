from django.urls import path, register_converter
from . import views, converters

register_converter(converters.TwoDigitsNumber, "nn") # Tipo de dato custom para urls dentro de django
register_converter(converters.ValidYearsConvert, "aaaa")


app_name = "libro_app"

urlpatterns = [
    path('api/autor/list', views.lista_autores.as_view()),
    path('api/autor/list/nacionalidad/<str:nacionalidad>/', views.FiltraAutores.as_view()),
    path('numero_mayor_a_15/<nn:nacionalidad>/<nn:pais>', views.FiltraPorNumero.as_view()),
    path('api/libros/list/posterior/<aaaa:year>/', views.ListarLibrosPosteriores.as_view()),
    path('numero_mayor_a_15/sin_converter/<nacionalidad>', views.FiltraPorNumero.as_view()),
    path('api/libros/titulo/', views.LibrosPorTitulo.as_view()),
    path('api/libros_fecha/titulo/', views.FiltrarLibros.as_view()), # http://127.0.0.1:8000/api/libros_fecha/titulo/?titulo=Halo&ano=2025
    path('api/libros_filtrar/autor/', views.LibrosAutor.as_view()),
    path('api/autor/detail/<pk>/', views.DetailAutor.as_view())
]


## Todos los endpoints que no se validen de forma correcta regresa por defecto un 404, es mejor para el servidor
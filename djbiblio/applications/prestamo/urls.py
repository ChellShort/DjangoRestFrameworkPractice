from django.urls import path
from . import views
app_name = "prestamo_app"

urlpatterns = [
    path('api/devoluciones/list', views.lista_devoluciones.as_view()),
    path('api/prestamos/list', views.lista_prestamos.as_view()),
    path('api/prestamos/list/fecha', views.lista_prestamos_fecha.as_view())
]

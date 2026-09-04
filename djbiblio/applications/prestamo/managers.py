from django.db import models

class DevolucionManager(models.Manager):
    def listar_devoluciones_all(self):
        return self.all()
    
class PrestamoManager(models.Manager):
    def listar_prestamos_all(self):
        return self.all()
    
    def listar_prestamos_fecha(self, fecha:str, libro:int):
        return self.filter(fecha__lte = fecha,
                           libro= libro) # lo mismo que: fecha = fecha ... curioso utiliza el nombre del campo no del tipo de dato fecha__lte != date__lte
    
    
    
    
from django.db import models

class Empleado(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)    
    estado = models.CharField(max_length=20)

    # funcion para imprimir datos del modelo
    def __str__(self):
        return f"{self.nombre} {self.estado} ({self.codigo})"
    
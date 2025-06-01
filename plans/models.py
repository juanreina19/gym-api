from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.IntegerField()
    acceso_piscina = models.BooleanField(default=False)
    acceso_clases_grupales = models.BooleanField(default=False)
    acceso_personal_trainer = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
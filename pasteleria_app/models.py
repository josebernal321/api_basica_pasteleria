from django.db import models
from django.utils import timezone
# Create your models here.


class Pasteles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    dificultad = models.CharField(max_length=50)
    fecha = models.DateField(default=timezone.now)
    img = models.CharField(max_length=300)
    estado = models.BooleanField(default=True)

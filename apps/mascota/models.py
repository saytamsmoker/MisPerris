from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	estado = models.CharField(max_length=11)
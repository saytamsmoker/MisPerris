from django.db import models

# Create your models here.

class Contacto(models.Model):
	rut = models.CharField(max_length=12)
	com_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=13)
	reg = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
    
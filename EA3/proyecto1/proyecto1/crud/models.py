from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.TextField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre
from django.db import models
# si definen un modelo nuevo deberan ejecutar makemigrations y migrate
# para que traspase el modelo a la base de datos


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


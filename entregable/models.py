from django.db import models

# Create your models here.

class Usuario(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)


    # metodo que tienen las clases en python para poder mostrar
    # determinado texto cuando hagamos el print de un objeto
    def __str__(self) -> str:
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido, self.creditos)
    
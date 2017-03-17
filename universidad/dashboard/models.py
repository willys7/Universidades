from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    numero_alumnos = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=255)

class Alumno(models.Model):
	nombre = models.CharField(max_length=255)
	carnet = models.IntegerField()
	edad = models.IntegerField()
	cursos = ListField(EmbeddedModelField('Curso'))
	carrera = models.CharField(max_length=255)


from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField
from .forms import ObjectListField

# Create your models here.
class EmbedOverrideField(EmbeddedModelField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, ObjectListField, **kwargs)

class Alumno(models.Model):
	cursos = EmbedOverrideField('Curso')
	nombre = models.CharField(max_length=255)
	carnet = models.IntegerField()
	edad = models.IntegerField()
	carrera = models.CharField(max_length=255)
	def __unicode__(self):
		return '%s %s %s %s (%s)' % (self.cursos.nombre, self.cursos.numero_alumnos, self.cursos.fecha, self.cursos.codigo, self.nombre, self.carnet, self.edad, self.carrera)

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    numero_alumnos = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=255, unique=True)
    def __unicode__(self):
		return '%s %s %s %s' % (self.nombre, self.numero_alumnos, self.fecha, self.codigo)
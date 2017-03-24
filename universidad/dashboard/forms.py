from django import forms
from dashboard.models import Alumno, Curso, Profesor

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ('nombre', 'numero_alumnos','codigo')

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'carnet', 'edad','carrera')

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'edad', 'username')

class ClaseForm(forms.Form):
	profesor = forms.CharField()
	curso = forms.CharField()
	estudiantes = forms.CharField()

class ClaseEditForm(forms.Form):
	seccion = forms.CharField()
	profesor = forms.CharField()
	curso = forms.CharField()
	estudiantes = forms.CharField()

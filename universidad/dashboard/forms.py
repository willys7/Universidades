from django import forms
from dashboard.models import Alumno, Curso, Profesor

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ('nombre', 'numero_alumnos','codigo')

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('cursos', 'nombre', 'carnet', 'edad','carrera')

class ProfesorForm(forms.ModelForm):
	cursos = forms.MultipleChoiceField(
		widget=forms.widgets.CheckboxSelectMultiple(), 
		required=False)
	class Meta:
		model = Profesor
		fields = ('username', 'nombre', 'edad', 'cursos')

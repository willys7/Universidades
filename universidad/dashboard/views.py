from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from dashboard.models import Curso, Alumno

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from dashboard.forms import CursoForm, AlumnoForm


def CursoList(request):

    cursos = Curso.objects.all()

    return render(
        request,
        'dashboard/curso_list.html',
        {
            'cursos': cursos
        }
    )

def CursoNew(request):
	curso_form = CursoForm()
	if request.method == 'GET':
	    curso_form = CursoForm()
	elif request.method == 'POST':
	    curso_form = CursoForm(data=request.POST)
	    if curso_form.is_valid():
	        curso_form.save()
	        curso_form = CursoForm()


	return render(
	    request,
	    'dashboard/curso_form.html',
	    {
	        'curso_form': curso_form
	    }
	)

def CursoEdit(request, curso_codigo):
	curso = Curso.objects.get(codigo=curso_codigo)
	message = ''
	if request.method == 'GET':
	    curso_form = CursoForm(instance=curso)

	elif request.method == 'POST':
	    curso_form = CursoForm(request.POST)
	    message = "Persona exitosamente guardada"
	    Curso.objects.get(codigo=curso_codigo).delete()
	    if curso_form.is_valid():
	        curso.nombre = curso_form.instance.nombre
	        curso.numero_alumnos = curso_form.instance.numero_alumnos
	        curso.codigo = curso_form.instance.codigo
	        curso.save()
	        print curso
	else:
	    pass

	return render(
	    request,
	    'dashboard/curso_form.html',
	    {
	        'curso_form': curso_form,
	        'message': message
	    }
	)
def CursoDelete(request, curso_codigo):
	curso = Curso.objects.get(codigo=curso_codigo)
	menssage = ''
	if(curso != None ):
		message = 'Se ha eliminiado el curso'
		Curso.objects.get(codigo=curso_codigo).delete()
	else:
		message = 'No se ha eliminiado el curso'

	cursos = Curso.objects.all()

	return render(
        request,
        'dashboard/curso_list.html',
        {
            'cursos': cursos,
            'message': message
        }
    )
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from dashboard.models import Curso, Alumno

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from dashboard.forms import CursoForm, AlumnoForm

#CRUD CURSO
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

#CRUD Alumno
def AlumnoList(request):

    alumnos = Alumno.objects.all()

    return render(
        request,
        'dashboard/alumno_list.html',
        {
            'alumnos': alumnos
        }
    )

def AlumnoNew(request):
	alumno_form = AlumnoForm()
	if request.method == 'GET':
	    alumno_form = AlumnoForm()
	elif request.method == 'POST':
	    alumno_form = AlumnoForm(data=request.POST)
	    if alumno_form.is_valid():
	        alumno_form.save()
	        alumno_form = AlumnoForm()


	return render(
	    request,
	    'dashboard/alumno_form.html',
	    {
	        'alumno_form': alumno_form
	    }
	)

def AlumnoEdit(request, alumno_codigo):
	alumno = Alumno.objects.get(carnet=alumno_codigo)
	message = ''
	if request.method == 'GET':
	    alumno_form = AlumnoForm(instance=alumno)

	elif request.method == 'POST':
	    alumno_form = AlumnoForm(request.POST)
	    message = "Alumno exitosamente guardado"
	    Alumno.objects.get(carnet=alumno_codigo).delete()
	    if alumno_form.is_valid():
	        alumno.nombre = alumno_form.instance.nombre
	        alumno.carnet = alumno_form.instance.carnet
	        alumno.edad = alumno_form.instance.edad
	        alumno.carrera = alumno_form.instance.carrera
	        alumno.save()
	        print alumno
	else:
	    pass

	return render(
	    request,
	    'dashboard/alumno_form.html',
	    {
	        'alumno_form': alumno_form,
	        'message': message
	    }
	)
def AlumnoDelete(request, curso_codigo):
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

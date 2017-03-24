from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from dashboard.models import Curso, Alumno, Profesor, Clase

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import simplejson as json

from dashboard.forms import CursoForm, AlumnoForm, ProfesorForm, ClaseForm, ClaseEditForm

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
def AlumnoDelete(request, alumno_codigo):
	alumnos = Alumno.objects.get(carnet=alumno_codigo)
	menssage = ''
	if(alumnos != None ):
		message = 'Se ha eliminiado el alumno'
		Alumno.objects.get(carnet=alumno_codigo).delete()
	else:
		message = 'No se ha eliminiado el alumno'

	alumnos = Alumno.objects.all()

	return render(
        request,
        'dashboard/alumno_list.html',
        {
            'alumnos': alumnos,
            'message': message
        }
    )

#CRUD PROFESOR

def ProfesorList(request):

    profesor = Profesor.objects.all()

    return render(
        request,
        'dashboard/profesor_list.html',
        {
            'profesor': profesor
        }
    )

def ProfesorNew(request):
	profesor_form = ProfesorForm()
	if request.method == 'GET':
	    profesor_form = ProfesorForm()
	elif request.method == 'POST':
	    profesor_form = ProfesorForm(data=request.POST)
	    if profesor_form.is_valid():
	        profesor_form.save()
	        profesor_form = ProfesorForm()


	return render(
	    request,
	    'dashboard/profesor_form.html',
	    {
	        'profesor_form': profesor_form
	    }
	)

def ProfesorEdit(request, profesor_codigo):
	profesor = Profesor.objects.get(username=profesor_codigo)
	message = ''
	if request.method == 'GET':
	    profesor_form = ProfesorForm(instance=profesor)

	elif request.method == 'POST':
	    profesor_form = ProfesorForm(request.POST)
	    message = "Profesor exitosamente guardado"
	    Profesor.objects.get(username=profesor_codigo).delete()
	    if profesor_form.is_valid():
	        profesor.nombre = profesor_form.instance.nombre
	        profesor.edad = profesor_form.instance.edad
	        profesor.username = profesor_form.instance.username
	        profesor.save()
	        print profesor
	else:
	    pass

	return render(
	    request,
	    'dashboard/profesor_form.html',
	    {
	        'profesor_form': profesor_form,
	        'message': message
	    }
	)
def ProfesorDelete(request, profesor_codigo):
	profesor = Profesor.objects.get(username=profesor_codigo)
	menssage = ''
	if(profesor != None ):
		message = 'Se ha eliminiado el profesor'
		Profesor.objects.get(username=profesor_codigo).delete()
	else:
		message = 'No se ha eliminiado el profesor'

	profesor = Profesor.objects.all()

	return render(
        request,
        'dashboard/profesor_list.html',
        {
            'profesor': profesor,
            'message': message
        }
    )

def ClaseList(request):

    clases = Clase.objects.all()

    return render(
        request,
        'dashboard/clase_list.html',
        {
            'clases': clases
        }
    )

def ClaseAlumnoList(request, seccion):

    clase = Clase.objects.get(seccion=seccion)

    return render(
        request,
        'dashboard/clase_alumnos_list.html',
        {
            'clase': clase,
            'alumnos': clase.estudiantes
        }
    )

def ClaseNew(request):
	clase_form = ClaseForm()
	if request.method == 'GET':
	    clase_form = ClaseForm()
	elif request.method == 'POST':
	    clase_form = ClaseForm(data=request.POST)
	    if clase_form.is_valid():
	    	profesor = clase_form.cleaned_data['profesor']
	    	curso = clase_form.cleaned_data['curso']
	    	carnets = clase_form.cleaned_data['estudiantes']
	    	print(profesor, curso)
	    	curso = Curso.objects.get(codigo=curso)
	    	profesor = Profesor.objects.get(username=profesor)
	    	print(profesor, curso)

	    	carnets = carnets.split(',')
	    	listEstudiantes = []
	    	for i in carnets:
	    		alumno = Alumno.objects.get(carnet=i.strip())
	    		print(alumno)
	    		listEstudiantes.append(alumno)

	    	print(listEstudiantes)

	    	seccion = curso.nombre + str(len(Clase.objects.all()))
	    	clase = Clase(curso=curso, profesor=profesor, seccion=seccion, estudiantes=listEstudiantes)
	    	print(clase)
	    	clase.save()
	    	clase_form = ClaseForm()


	return render(
	    request,
	    'dashboard/clase_form.html',
	    {
	        'clase_form': clase_form
	    }
	)

def ClaseDelete(request, seccion):
	profesor = Clase.objects.get(seccion=seccion)
	menssage = ''
	if(clase != None ):
		message = 'Se ha eliminiado el clase'
		Clase.objects.get(seccion=seccion).delete()
	else:
		message = 'No se ha eliminiado el clase'

	clases = Clase.objects.all()

	return render(
        request,
        'dashboard/clase_list.html',
        {
            'clases': clases,
            'message': message
        }
    )

def ClaseEdit(request, seccion):
	clase = Clase.objects.get(seccion=seccion)
	message = ''
	if request.method == 'GET':
		estudiantes = ''
		h = 0
		for i in clase.estudiantes:
			print(i)
			estudiantes += str(i.carnet)
			h += 1
			if not (h == len(clase.estudiantes)):
				estudiantes += ','
		print(estudiantes)
		data = {'seccion':clase.seccion, 'curso': clase.curso.codigo, 'profesor': clase.profesor.username, 'estudiantes':estudiantes}
		clase_form = ClaseEditForm(initial=data)
	elif request.method == 'POST':
	    clase_form = ClaseEditForm(request.POST)
	    message = "Clase exitosamente guardado"
	    Clase.objects.get(seccion=seccion).delete()
	    if clase_form.is_valid():
	    	profesor = clase_form.cleaned_data['profesor']
	    	curso = clase_form.cleaned_data['curso']
	    	seccion = clase_form.cleaned_data['seccion']
	    	carnets = clase_form.cleaned_data['estudiantes']
	    	print(profesor, curso)
	    	curso = Curso.objects.get(codigo=curso)
	    	profesor = Profesor.objects.get(username=profesor)
	    	print(profesor, curso)

	    	carnets = carnets.split(',')
	    	listEstudiantes = []
	    	for i in carnets:
	    		alumno = Alumno.objects.get(carnet=i.strip())
	    		print(alumno)
	    		listEstudiantes.append(alumno)

	    	print(listEstudiantes)
	    	clase = Clase(curso=curso, profesor=profesor, seccion=seccion, estudiantes=listEstudiantes)
	    	clase.save()
	else:
	    pass

	return render(
	    request,
	    'dashboard/clase_form.html',
	    {
	        'clase_form': clase_form,
	        'message': message
	    }
	)

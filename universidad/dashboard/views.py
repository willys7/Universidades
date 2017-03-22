from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from dashboard.models import Curso, Alumno

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from dashboard.forms import CursoForm, AlumnoForm, ProfesorForm


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

#def CursoEdit(request, codigo):

def ProfesorNew(request):
	add_profesor = ProfesorForm()
	if request.method == 'GET':
	    add_profesor = ProfesorForm()
	elif request.method == 'POST':
	    add_profesor = ProfesorForm(data=request.POST)
	    if add_profesor.is_valid():
	        add_profesor.save()
	        add_profesor = ProfesorForm()


	return render(
	    request,
	    'dashboard/add_profesor.html',
	    {
	        'add_profesor': add_profesor
	    }
	)
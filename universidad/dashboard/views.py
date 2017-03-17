from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from dashboard.models import Curso, Alumno

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy




class CursoList(ListView):
    model = Curso

class CursoCreate(CreateView):
    model = Curso
    fields = ['nombre', 'numero_alumnos','fecha','codigo']
    success_url = reverse_lazy('dashboard:curso_list')

class CursoUpdate(UpdateView):
    model = Curso
    fields = ['nombre', 'numero_alumnos','fecha','codigo']
    success_url = reverse_lazy('dashboard:curso_list')

class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('dashboard:curso_list')


class AlumnoList(ListView):
    model = Alumno

class AlumnoCreate(CreateView):
    model = Alumno
    fields = ['nombre', 'numero_alumnos','fecha','codigo']
    success_url = reverse_lazy('dashboard:alumno_list')

class AlumnoUpdate(UpdateView):
    model = Alumno
    fields = ['nombre', 'numero_alumnos','fecha','codigo']
    success_url = reverse_lazy('dashboard:alumno_list')

class AlumnoDelete(DeleteView):
    model = Alumno
    success_url = reverse_lazy('dashboard:alumno_list')
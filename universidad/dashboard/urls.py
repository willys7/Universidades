from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CursoList.as_view(), name='curso_list'),
	url(r'^new$', views.CursoCreate.as_view(), name='curso_new'),
	url(r'^edit/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='curso_edit'),
	url(r'^delete/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='curso_delete'),

	url(r'^$', views.AlumnoList.as_view(), name='alumno_list'),
	url(r'^alumno/new$', views.AlumnoCreate.as_view(), name='alumno_new'),
	url(r'^alumno/edit/(?P<pk>\d+)$', views.AlumnoUpdate.as_view(), name='alumno_edit'),
	url(r'^alumno/delete/(?P<pk>\d+)$', views.AlumnoDelete.as_view(), name='alumno_delete'),
]
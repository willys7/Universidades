from django.conf.urls import url


from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^curso/$', dashboard_views.CursoList, name='curso_list'),
    url(r'^curso/new/$', dashboard_views.CursoNew, name='curso_new'),
    url(r'^curso/(?P<curso_codigo>[0-9]+)/edit_curso/$', dashboard_views.CursoEdit, name='curso_edit'),
    url(r'^curso/(?P<curso_codigo>[0-9]+)/eliminar_curso/$', dashboard_views.CursoDelete, name='curso_delete'),
    url(r'^alumno/new/$', dashboard_views.AlumnoNew, name='alumno_new'),
    url(r'^alumno/$', dashboard_views.AlumnoList, name='alumno_list'),
    url(r'^alumno/(?P<alumno_codigo>[0-9]+)/edit_alumno/$', dashboard_views.AlumnoEdit, name='alumno_edit'),
]
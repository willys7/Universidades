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
    url(r'^alumno/(?P<alumno_codigo>[0-9]+)/eliminar_alumno/$', dashboard_views.AlumnoDelete, name='alumno_delete'),
    url(r'^profesor/new/$', dashboard_views.ProfesorNew, name='profesor_new'),
    url(r'^profesor/$', dashboard_views.ProfesorList, name='profesor_list'),
    url(r'^profesor/(?P<profesor_codigo>.+)/edit_profesor/$', dashboard_views.ProfesorEdit, name='profesor_edit'),
    url(r'^profesor/(?P<profesor_codigo>.+)/eliminar_profesor/$', dashboard_views.ProfesorDelete, name='profesor_delete'),
    url(r'^clase/$', dashboard_views.ClaseList, name='clase_list'),
    url(r'^clase/(?P<seccion>.+)/alumnos$', dashboard_views.ClaseAlumnoList, name='clase_alumnos_list'),
    url(r'^clase/new/$', dashboard_views.ClaseNew, name='clase_new'),
    url(r'^clase/(?P<seccion>.+)/edit_clase/$', dashboard_views.ClaseEdit, name='clase_edit'),
    url(r'^clase/(?P<seccion>.+)/eliminar_clase/$', dashboard_views.ClaseDelete, name='clase_delete'),
]
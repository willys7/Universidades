from django.conf.urls import url


from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.CursoList, name='curso_list'),
    url(r'^new/$', dashboard_views.CursoNew, name='curso_new'),
    url(r'^(?P<curso_codigo>[0-9]+)/edit_curso/$', dashboard_views.CursoEdit, name='curso_edit'),
    url(r'^(?P<curso_codigo>[0-9]+)/eliminar_curso/$', dashboard_views.CursoDelete, name='curso_delete'),
]
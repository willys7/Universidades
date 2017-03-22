from django.conf.urls import url


from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^$', dashboard_views.CursoList, name='curso_list'),
    url(r'^new/$', dashboard_views.CursoNew, name='curso_new'),
    url(r'^new/profesor$', dashboard_views.ProfesorNew, name='add_profesor'),
]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^control/$', views.control, name='control'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^people/$', views.people, name='people'),
    url(r'^logged_out/$', views.logged_out, name='logged_out'),
]

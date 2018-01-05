from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^history/$', views.history, name='history'),
    url(r'^control/$', views.control, name='control'),
]

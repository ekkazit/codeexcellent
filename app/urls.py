from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.service, name='service'),
    url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^contact/$', views.contact, name='contact'),
]

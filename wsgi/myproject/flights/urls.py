from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'check', views.check, name='check'),
    url(r'createsubscriber', views.createsubscriber, name='createsubscriber'),
    
]
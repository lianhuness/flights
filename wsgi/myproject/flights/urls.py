from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.check, name='index'),
    url(r'check', views.check, name='check'),
]
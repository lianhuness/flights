from django.conf.urls import url

from . import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
	url('^', include('django.contrib.auth.urls'))
    # url(r'login', views.login, name='login'),
    # url(r'logout', views.logout, name='logout'),
    # url(r'newuser', views.newuser, name='newuser'),    
    # url(r'resetpwd', views.resetpwd, name='resetpwd')
]
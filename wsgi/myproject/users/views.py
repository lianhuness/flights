#coding=utf8
import requests
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
# Create your views here.
import datetime
from datetime import date

def login(request):
	return render(request, 'users/login.html')

def logout(request):
	return render(request, 'users/logout.html')
	
def newuser(request):
	return render(request, 'users/newuser.html')

def resetpwd(request):
	return render(request, 'users/resetpwd.html')
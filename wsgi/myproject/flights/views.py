from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
# Create your views here.
import datetime
from datetime import date

import json

import pdb


def check(request):
	return render(request, 'flights/check.html')
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
# Create your views here.
import datetime
from datetime import date

import json

import pdb

import utils

def check(request):
	if request.method == "GET":
		return render(request, 'flights/check.html')
	else:
		try:
			fromPort = request.POST['fromPort']
			toPort = request.POST['toPort']
			flightDate = request.POST['date']
			fromPort = fromPort.split('-')[-1].strip()
			toPort = toPort.split('-')[-1].strip()
			
			day = datetime.datetime.strptime(str(flightDate), "%m/%d/%Y");
			print(day)
			data = utils.UAFlight(fromPort, toPort, day)
			if len(data) is 0:
				return HttpResponse("No Flight Found")
			else:
				return HttpResponse(json.dumps(data))
		except:
			return HttpResponse("ERROR here")
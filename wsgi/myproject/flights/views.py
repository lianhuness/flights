from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
# Create your views here.
import datetime
from datetime import date

import json

import pdb

#coding=utf8
import requests
import pdb
import json
import datetime 



def UAFlight(origin, destination, day):
    print("Flight check: %s" % day)
    print(origin)
    print(destination)
    print(day)
    output = []
    url = 'https://www.united.com/ual/en/us/flight-search/book-a-flight/flightshopping/getflightresults/awd'
    s = requests.Session()
    headers = {'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                             'X-Requested-With': 'XMLHttpRequest'}

    daystr = day.strftime("%b %-d, %Y")
    wdaystr = day.strftime("%a, %b %-d, %Y")
    print(daystr)
    print(wdaystr)

    
    data='{"Revise":false,"UnaccompaniedMinorDisclamer":false,"searchTypeMain":"oneWay",'
    data += '"Origin":"%s"' % origin
    data += ',"Destination":"%s"'% destination
    data += ',"DepartDate":"%s"' % daystr
    data += ',"awardTravel":true,"MaxTrips":null,"numberOfTravelers":2,"numOfAdults":2,"numOfSeniors":0,"numOfChildren03":0,"numOfChildren02":0,"numOfChildren01":0,"numOfInfants":0,"numOfLapInfants":0,"travelerCount":2,"IsUnAccompaniedMinor":false,"MilitaryTravelType":null,"MilitaryOrGovernmentPersonnelStateCode":null,"tripLength":0,"flexMonth":null,"flexMonth2":null,"SortType":"bestmatches","cboMiles":null,"cboMiles2":null,"Trips":[{"DestinationAll":false,"returnARC":null,"connections":null,"nonStopOnly":true,"nonStop":true,"oneStop":false,"twoPlusStop":false,'
    data += '"DepartDate":"%s"' % daystr
    data += ',"ReturnDate":null,"PetIsTraveling":false,"PreferredTime":"","PreferredTimeReturn":null,'
    data += '"Destination":"%s"' % destination
    data += ',"Index":1,'
    data += '"Origin":"%s"' % origin
    data += ',"Selected":false,"FormatedDepartDate":"%s"' % wdaystr
    data += ',"OriginCorrection":null,"DestinationCorrection":null,"OriginAll":false}],"nonStopOnly":false,"CalendarOnly":false,"InitialShop":true,"IsSearchInjection":false,"CartId":"","CellIdSelected":null,"BBXSession":null,"SolutionSetId":null,"SimpleSearch":true,"RequeryForUpsell":false,"RequeryForPOSChange":false,"ShowClassOfServiceListPreference":false,"SelectableUpgradesOriginal":null,"RegionalPremierUpgradeBalance":0,"GlobalPremierUpgradeBalance":0,"RegionalPremierUpgrades":null,"GlobalPremierUpgrades":null,"FormattedAccountBalance":null,"GovType":null,"TripTypes":1,"flexible":false,"flexibleAward":false,"FlexibleDaysAfter":0,"FlexibleDaysBefore":0,"hiddenPreferredConn":null,"hiddenUnpreferredConn":null,"carrierPref":0,"chkFltOpt":0,"portOx":0,"travelwPet":0,"NumberOfPets":0,"cabinType":1,"cabinSelection":"BUSINESS","awardCabinType":1,"FareTypes":0,"FareWheelOnly":false,"buyUpgrade":0,"offerCode":null,"TVAOfferCodeLastName":null,"ClassofService":null,"UpgradeType":null,"BillingAddressCountryCode":null,"BillingAddressCountryDescription":null,"IsPassPlusFlex":false,"IsPassPlusSecure":false,"IsOffer":false,"IsMeetingWorks":false,"IsValidPromotion":false,"CalendarDateChange":null,"CoolAwardSpecials":false,"LastResultId":null,"IncludeLmx":false}'
    r = s.post(url, data=data, headers = headers)
    text = r.text
    print(text)
    obj = json.loads(text)
    print(" \n\n\n =============== %s ============== \n\n" % daystr)
    print(len(obj['data']['Trips']))
    
    flights = obj['data']['Trips'][0]['Flights']
    print("Total flights: %s " % len(flights))

    
    for flight in flights:
        pc = flight['PricesByColumn']
        finfo = {}
        fields = ['Index', 'DepartDateTime', 'AirportsStopList', 'Destination', 'FlightNumber', 'PricesByColumn']
        for fld in fields:
            if fld in flight:
                finfo[fld] = flight[fld]
            else:
                finfo[fld] = None
        finfo['rawData'] = json.dumps(flight)
        output.append(finfo)
    return output

@ensure_csrf_cookie
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
			data = UAFlight(fromPort, toPort, day)
			if len(data) is 0:
				return HttpResponse("No Flight Found")
			else:
				return HttpResponse(json.dumps(data))
		except:
			return HttpResponse("ERROR here")
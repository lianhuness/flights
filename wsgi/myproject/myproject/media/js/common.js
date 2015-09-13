function setCookie(cname, cvalue, exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = "expires="+d.toUTCString();
	document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname) {
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i=0; i<ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1);
		if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
	}
	return "";
}
function test(){
	alert("it's a test");
}
function checkCookie() {
	var user = getCookie("username");
	if (user != "") {
		alert("Welcome again " + user);
	} else {
		user = prompt("Please enter your name:", "");
		if (user != "" && user != null) {
			setCookie("username", user, 365);
		}
	}
}

function getStops(stopObj)
{
	if(stopObj.length == 0)
		return "Non-Stop";
	else{
		var output = "";
		for(var i in stopObj)
		{
			if(output.length > 0)
				output+= " - ";
			output+= stopObj[i]['Description'];
		}
		return ""+stopObj.length + ": " + output;
	}
}
function getBestEcomic(PricesByColumn)
{
	var output = 0;
	if(PricesByColumn['MIN-ECONOMY-SURP-OR-DISP'] &&
		PricesByColumn['MIN-ECONOMY-SURP-OR-DISP'] > output)
		return parseInt(PricesByColumn['MIN-ECONOMY-SURP-OR-DISP']);
	return "Not Available";	
}
function getBestBusiness(PricesByColumn)
{
	var var1 = 0;
	var var2 = 0;
	if(PricesByColumn['BUSINESS-DISPLACEMENT'] &&
		PricesByColumn['BUSINESS-DISPLACEMENT'] > 0)
		var1 = PricesByColumn['BUSINESS-DISPLACEMENT'];

	if(PricesByColumn['BUSINESS-SURPLUS'] &&
		PricesByColumn['BUSINESS-SURPLUS'] > 0)
		var2 = PricesByColumn['BUSINESS-SURPLUS'];

	if(var1 == 0 && var2 == 0)
		return "Not Available";

	if(var1 > 0 && var2 > 0)
		return var1 < var2 ? var1: var2;
	return var1 == 0? var2: var1;
}

function getBestFirst(PricesByColumn)
{
	var var1 = 0;
	var var2 = 0;
	if(PricesByColumn['FIRST-DISPLACEMENT'] &&
		PricesByColumn['FIRST-DISPLACEMENT'] > 0)
		var1 = PricesByColumn['FIRST-DISPLACEMENT'];

	if(PricesByColumn['FIRST-SURPLUS'] &&
		PricesByColumn['FIRST-SURPLUS'] > 0)
		var2 = PricesByColumn['FIRST-SURPLUS'];

	if(var1 == 0 && var2 == 0)
		return "Not Available";

	if(var1 > 0 && var2 > 0)
		return var1 < var2 ? var1: var2;
	return var1 == 0? var2: var1;
}

$(document).ready(function() {
//set initial state.


});
from django.db import models


# Create your models here.
class User(models.Model):
	email = models.EmailField(max_length='100')
	name = models.CharField(max_length='100')

class Subscriber(models.Model):
	user = models.ForeignKey(User)
	status = models.CharField(max_length='10', default='INACTIVE')
	fromAirport = models.CharField(max_length='100')
	toAirport = models.CharField(max_length='100')
	startDate = models.DateField()
	endDate = models.DateField()

class FlightResult(models.Model):
	subscriber = models.ForeignKey(Subscriber)
	checkDate = models.DateField()
	results = models.TextField()



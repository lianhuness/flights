from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
	user = models.ForeignKey(User)
	status = models.CharField(max_length='10', default='INACTIVE')
	fromAirport = models.CharField(max_length='100')
	toAirport = models.CharField(max_length='100')
	startDate = models.DateField()
	endDate = models.DateField()

	def __str__(self):
		return "%s -> %s " %(self.fromAirport, self.toAirport)


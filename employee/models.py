from __future__ import unicode_literals
from django.db import models
from time import time

# Create your models here.

class Employee(models.Model):
	Employee_ID = models.TextField(max_length=254)
	Employee_Name = models.TextField(max_length=254)
	Date_Of_Joining = models.DateField()

	def __unicode__(self):
		return self.Employee_ID
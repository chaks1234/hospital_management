from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Reg(models.Model):
	name = models.CharField(max_length = 50)
	Password = models.CharField(max_length = 25)
	
	def __unicode__(self):
		return self.name

	
	
	
class Doctor(models.Model):
	name = models.CharField(max_length = 50)
	#password = models.CharField(max_length = 50)

	def get_absolute_url(self):
		return reverse('home:index')

	def __unicode__(self):
		return self.name
	
	
	
	
class Patient(models.Model):
	Teacher = models.ForeignKey(Doctor,on_delete= models.CASCADE)
	name = models.CharField(max_length = 50)
	adhar = models.CharField(max_length = 20)
	is_visited = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('home:patient')
	

	

	
	
	

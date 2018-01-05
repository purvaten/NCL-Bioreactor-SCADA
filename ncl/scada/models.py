from django.db import models

class Values(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	office = models.CharField(max_length=150)
	age = models.IntegerField()
	start_date = models.DateTimeField()
	salary = models.IntegerField()

	def __str__(self):
		return self.name

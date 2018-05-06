from django.db import models
import django


class Values(models.Model):
    """Class Values"""
    name = models.CharField(max_length=100, default="anonymous")
    start_date = models.DateTimeField(default=django.utils.timezone.now)
    pressure = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    ph = models.FloatField(default=0.0)
    levels = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

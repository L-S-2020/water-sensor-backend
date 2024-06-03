from django.db import models

# Create your models here.
class Data(models.Model):
    temperature = models.FloatField()
    speed = models.FloatField()
    ph = models.FloatField()
    turbidity = models.FloatField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)



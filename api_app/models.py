from django.db import models

class Planta(models.Model):
    humedad = models.IntegerField()
    temperatura = models.IntegerField()

# from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Prediction(models.Model):
    tahun = models.IntegerField()
    penduduk_perempuan = models.IntegerField()


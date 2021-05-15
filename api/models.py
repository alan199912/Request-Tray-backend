from django.db import models
from random import randrange
import datetime

class ApplyCreditUser(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField()
    lastName = models.TextField()
    salary = models.DecimalField(max_digits = 8, decimal_places = 2)
    creditDescription = models.TextField()
    credit = models.DecimalField(max_digits = 8, decimal_places = 2)
    status = models.IntegerField(default = 0)
    defaulter = models.IntegerField(default = randrange(10))
    indicator = models.IntegerField(default = randrange(10))
    date = models.DateField(default=datetime.date.today)


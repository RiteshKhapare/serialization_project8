from django.db import models

class Employee(models.Model):
    e_id = models.IntegerField(unique=True)
    e_name = models.CharField(max_length=25)
    age = models.IntegerField()
    sal = models.IntegerField()

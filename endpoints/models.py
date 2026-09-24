from django.db import models

class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    emp_ID = models.IntegerField(unique=True)
    age = models.IntegerField()
    
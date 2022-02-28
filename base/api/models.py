from operator import mod
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=120, default=True)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    mobile_name = models.CharField(max_length=120, default=True)
    model_name = models.CharField(unique=True,max_length=120, default=True)
    price = models.FloatField()
    description = models.TextField(max_length=255, default=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="by", default=True)

    def __str__(self):
        return self.mobile_name    
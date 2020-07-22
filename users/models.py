from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=254)
    telephone = models.CharField(max_length=254)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_telephone = models.CharField(max_length=254)
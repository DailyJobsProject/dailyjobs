from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


from django.core.files import File

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=254)
    telephone = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('users:company_detail', kwargs={'pk': self.pk})

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=254)


    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse_lazy('users:employee_detail', kwargs={'pk': self.pk})


class Document(models.Model):
    document = models.FileField(upload_to='media/', max_length=255, blank=True)
    description = models.CharField(max_length=50)






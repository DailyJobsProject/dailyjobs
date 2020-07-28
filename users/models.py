from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


from django.core.files import File

class User(AbstractUser):
    """user.is_company/is_employee are filled in backend through forms"""

    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Company(models.Model):
    """Company type user"""

    user = models.OneToOneField(User, primary_key=True, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, unique=True)
    telephone = models.CharField(max_length=254)
    about = models.TextField(max_length=1000, default='Tell us something about you')
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('users:company_detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    """Employee type user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=254)
    about = models.TextField(max_length=1000, default='Tell us something about you')
    image = models.ImageField(upload_to='profile_pics')
    cv = models.FileField(upload_to='CVs')

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse_lazy('users:employee_detail', kwargs={'pk': self.pk})


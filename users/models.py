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
    about = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('users:company_detail', kwargs={'pk': self.pk})

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return 'media/profile_pics/user.jpg'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=254)
    about = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='profile_pics', default='')
    


    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse_lazy('users:employee_detail', kwargs={'pk': self.pk})

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return 'media/profile_pics/user.jpg'

class Document(models.Model):
    document = models.FileField(upload_to='media/', max_length=255, blank=True)
    description = models.CharField(max_length=50)






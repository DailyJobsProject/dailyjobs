from django.db import models
from django.urls import reverse

# Create your models here.

from django.contrib.auth import get_user_model


User = get_user_model()


class CompanyPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    description = models.TextField(editable=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

class Application(models.Model):
    post = models.ForeignKey(CompanyPost, related_name='applications', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('users:employee_detail', kwargs={'pk': self.pk})



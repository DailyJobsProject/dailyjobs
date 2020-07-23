# from ..dailyjobs.dailyjobs.settings import MEDIA_ROOT
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
    # image = models.ImageField(upload_to=MEDIA_ROOT, default='/static/img/default.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})




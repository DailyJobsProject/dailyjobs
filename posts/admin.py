from django.contrib import admin

# Register your models here.
from .models import Application, CompanyPost

admin.site.register(Application)
admin.site.register(CompanyPost)
from django import forms
from .models import Application
from django.db import transaction

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = []

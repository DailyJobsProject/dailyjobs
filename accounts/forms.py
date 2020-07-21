from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Company, User
from django.contrib.auth import get_user_model

class CompanySignUpForm(UserCreationForm):
    name = forms.CharField(max_length=254, label='Company name')
    telephone = forms.CharField(max_length=254, label='Company telephone')


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'telephone']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user)
        company.name += self.clean()['name']
        company.telephone += self.clean()['telephone']
        company.save()
        return user

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Company, User, Employee
from django.contrib.auth import get_user_model

class CompanySignUpForm(UserCreationForm):
    name = forms.CharField(max_length=254, label='Company name')
    telephone = forms.CharField(max_length=254, label='Company telephone')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'telephone']

    def __init__(self, *args, **kwargs): # Removes helper text from UserCreationForm
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

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)
    telephone = forms.CharField(max_length=254, label='Employee telephone')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'telephone']

    def __init__(self, *args, **kwargs): # Removes helper text from UserCreationForm
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user = user)
        employee.first_name += self.clean()['first_name']
        employee.last_name += self.clean()['last_name']
        employee.telephone += self.clean()['telephone']
        employee.save()
        return user


class CompanyAboutUpdateForm(forms.ModelForm):
    about = forms.Textarea()

    class Meta:
        model = Company
        fields = ['about']

        widgets = {
            'about': forms.Textarea(attrs={'rows':10, 'cols':80}),
        }

class EmployeeUpdateForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['about', 'telephone']

        widgets = {
            'about': forms.Textarea(attrs={'rows':10, 'cols':80}),
        }

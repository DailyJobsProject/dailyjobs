from django import forms
from .models import Application, CompanyPost
from django.db import transaction

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = []

class CompanyPostForm(forms.ModelForm):
    title = forms.Textarea()
    description = forms.Textarea()
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)
    city = forms.CharField()

    class Meta:
        model = CompanyPost
        fields = ['title', 'description', 'city', 'start_date', 'end_date']

        widgets = {
            'title': forms.Textarea(attrs={'rows':2, 'cols':50}),
            'description': forms.Textarea(attrs={'rows':10, 'cols':80}),
        }

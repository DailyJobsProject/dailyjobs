from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, TemplateView, DetailView, 
                                  UpdateView)

from .forms import CompanySignUpForm, EmployeeSignUpForm
from .models import User, Company, Employee

from rest_framework import viewsets
from .serializers import CompanySerializer, EmployeeSerializer


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class LogInView(LoginView):
    template_name = 'registration/login.html'

class CompanySignUpView(CreateView):
    """SignUp view for Company-type user"""

    model = User
    form_class = CompanySignUpForm
    template_name = 'registration/company_signup_form.html'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class CompanyDetailView(LoginRequiredMixin, DetailView):
    """Detail View for Company"""

    model = Company
    template_name = "company_detail.html"

    def get_context_data(self, **kwargs):
        from django.apps import apps
        CompanyPost = apps.get_model('posts', 'CompanyPost')

        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context["my_posts"] = CompanyPost.objects.all()
        return context

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """Updates Company.about"""

    login_url = 'accounts/login'
    model = Company
    fields = ['about']
    template_name = 'company_update.html'

class CProfilePicUpdateView(LoginRequiredMixin, UpdateView):
    """Updates Company.image (profile picture)"""

    login_url = 'accounts/login'
    model = Company
    fields = ['image']
    template_name = 'cprofilepic_update.html'

class EmployeeSignUpView(CreateView):
    """SignUp view for Employee-type user"""

    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/employee_signup_form.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """Detail view for Employee"""

    model = Employee
    template_name = "employee_detail.html"

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """Updates Employee.about"""
    
    login_url = 'accounts/login'
    model = Employee
    fields = ['about']
    template_name = 'employee_update.html'

class EProfilePicUpdateView(LoginRequiredMixin,UpdateView):
    """Updates Employee.image (profile picture)"""

    login_url = 'accounts/login'
    model = Employee
    fields = ['image']
    template_name = 'eprofilepic_update.html'

class CVUpdateView(LoginRequiredMixin,UpdateView):
    """Updates Employee.cv"""

    login_url = 'accounts/login'
    model = Employee
    fields = ['cv']
    template_name = 'cv_update.html'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('user')
    serializer_class = EmployeeSerializer

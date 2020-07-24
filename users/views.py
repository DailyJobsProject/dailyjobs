from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CompanySignUpForm, EmployeeSignUpForm
from .models import User, Company, Employee
from django.urls import reverse_lazy

class CompanySignUpView(CreateView):
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

class EmployeeSignUpView(CreateView):
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

    

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class LogInView(TemplateView):
    template_name = 'registration/login.html'


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "company_detail.html"

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employee_detail.html"

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'accounts/login'
    model = Company
    fields = ['about']
    template_name = 'company_update.html'

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'accounts/login'
    model = Employee
    fields = ['about']
    template_name = 'employee_update.html'


class CProfilePicUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'accounts/login'
    model = Company
    fields = ['image']
    template_name = 'cprofilepic_update.html'

class EProfilePicUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'accounts/login'
    model = Employee
    fields = ['image']
    template_name = 'eprofilepic_update.html'

def image_upload_view(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'registration/upload.html', context)

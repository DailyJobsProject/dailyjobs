from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .forms import CompanySignUpForm, EmployeeSignUpForm
from .models import User
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
        return redirect('start_page.html')

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
        return redirect('start_page.html')

    

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class LogInView(TemplateView):
    template_name = 'registration/login.html'

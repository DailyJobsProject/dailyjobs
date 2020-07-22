from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignInView.as_view(), name= 'login'),
    path('signup/company', views.CompanySignUpView.as_view(), name='company_signup'),
    path('signup/employee', views.EmployeeSignUpView.as_view(), name='employee_signup'),
]

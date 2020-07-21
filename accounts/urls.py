from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.SignUpView.as_view, name='signup'),
    path('signup/company', views.CompanySignUpView.as_view(), name='company_signup'),
    path('signup/employee', views.EmployeeSignUpView.as_view(), name='employee_signup'),
]

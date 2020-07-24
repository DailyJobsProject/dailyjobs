from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name= 'login'),
    path('signup/company', views.CompanySignUpView.as_view(), name='company_signup'),
    path('signup/employee', views.EmployeeSignUpView.as_view(), name='employee_signup'),

    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/profile_pic/edit', views.CProfilePicUpdateView.as_view(), name='cprofilepic_update'),

    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/profile_pic/edit', views.EProfilePicUpdateView.as_view(), name='eprofilepic_update'),    
]

from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name= 'login'),
    path('signup/company', views.CompanySignUpView.as_view(), name='company_signup'),
    path('signup/employee', views.EmployeeSignUpView.as_view(), name='employee_signup'),

    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/profile_pic/edit', views.CProfilePicUpdateView.as_view(), name='cprofilepic_update'),

    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('upload', views.image_upload_view, name='upload'),

    
]

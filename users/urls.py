from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('users/', include(router.urls)),
    path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),

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
    path('employee/<int:pk>/cv/edit', views.CVUpdateView.as_view(), name='cv_update')
]

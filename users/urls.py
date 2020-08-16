from django.urls import path, include
from posts.views import ApplicationViewSet, CompanyPostViewSet
from . import views
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'company_posts', CompanyPostViewSet)

urlpatterns = [
    # Template Views
    path('', views.WelcomePage.as_view(), name='welcome'),
    path('about', views.AboutPage.as_view(), name='about'),

    # Rest API
    path('rest/', include(router.urls)),

    # Registration / Login
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/company', views.CompanySignUpView.as_view(), name='company_signup'),
    path('signup/employee', views.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('login/', views.LogInView.as_view(), name= 'login'),
    path('login_redirect', views.user_redirect, name='userredirect'),
    path('logout/', views.LogOutView.as_view(), name='logged_out'),

    # Company profile
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/profile_pic/edit', views.CProfilePicUpdateView.as_view(), name='cprofilepic_update'),

    # Employee profile
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/profile_pic/edit', views.EProfilePicUpdateView.as_view(), name='eprofilepic_update'),
    path('employee/<int:pk>/cv/edit', views.CVUpdateView.as_view(), name='cv_update'),
    path('employee/<int:pk>/contact_info/edit', views.EmployeeContactUpdateView.as_view(), name='contact_info'),
]

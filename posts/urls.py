from django.urls import path, include
from rest_framework import routers
from .views import ApplicationViewSet, CompanyPostViewSet
from . import views




app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name ='detail'),
    path('list/', views.PostListView.as_view(), name ='list'),
    path('employee_applications/', views.EmployeeApplicationsListView.as_view(), name='employee_applications_list'),
    path('<int:pk>/post_delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/post_update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/apply/', views.post_apply, name='apply'),
    path('<int:pk>/application_delete/', views.ApplicationDeleteView.as_view(), name='application_delete'),
]

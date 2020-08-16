from django.urls import path, include
from . import views


app_name = 'posts'

urlpatterns = [


    # Company Post URLs for Company
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name ='detail'),
    path('<int:pk>/post_delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/post_update/', views.PostUpdateView.as_view(), name='update'),

    # Company Post URLs for Employee
    path('<int:pk>/apply/', views.post_apply, name='apply'),
    path('<int:pk>/application_delete/', views.ApplicationDeleteView.as_view(), name='application_delete'),
    path('employee_applications/', views.EmployeeApplicationsListView.as_view(), name='employee_applications_list'),

    # List of all Company Posts
    path('list/', views.PostListView.as_view(), name ='list'),

    # Company Posts list search URL
    path('search', views.SearchView.as_view(), name='search'),
]

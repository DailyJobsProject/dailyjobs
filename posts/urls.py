from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('list/', views.PostListView.as_view(), name = 'list'),

]
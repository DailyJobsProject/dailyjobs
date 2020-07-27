from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('list/', views.PostListView.as_view(), name = 'list'),
    path('<int:pk>/post_delete', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/post_update', views.PostUpdateView.as_view(), name='update'),

]

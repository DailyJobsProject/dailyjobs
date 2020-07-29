from django.urls import path, include
from rest_framework import routers
from .views import ApplicationViewSet, CompanyPostViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'company_posts', CompanyPostViewSet)



app_name = 'posts'

urlpatterns = [
    path('', include(router.urls)),
    path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('list/', views.PostListView.as_view(), name = 'list'),
    path('<int:pk>/post_delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/post_update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/apply/', views.post_apply, name='apply'),
    path('<int:pk>/application_delete/', views.ApplicationDeleteView.as_view(), name='application_delete')
]

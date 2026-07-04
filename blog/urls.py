from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, CategoryListAPIView

urlpatterns = [
    path('api/posts/', PostListAPIView.as_view(), name ='post-list-api'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name = 'post-detail-api'),
    path('api/categories/', CategoryListAPIView.as_view(), name= 'category-list-api')

]


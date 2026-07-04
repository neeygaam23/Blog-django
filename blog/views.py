from rest_framework import generics
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
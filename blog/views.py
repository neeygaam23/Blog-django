from rest_framework import generics
from .models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post__id = post_id)
    
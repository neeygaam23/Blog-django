from rest_framework import serializers
from .models import Post, Category , Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content','created_at','author','category']
        depth = 1 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','post','author','body','created_at']
        read_only_fields= ['post','author','created_at']

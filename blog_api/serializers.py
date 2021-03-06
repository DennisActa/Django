from rest_framework import serializers
from blog.models import Post, Category
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class PostSerializer(serializers.ModelSerializer):
    authorUserName = serializers.CharField(read_only=True, source="author.username")
    categoryName = serializers.CharField(read_only=True, source="category.name")

    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'image', 'slug', 'author', 'excerpt', 'content', 'status', 'published', 'authorUserName', 'categoryName')


# class FrontendPostSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer(many=False, read_only=True)
#     category = CategorySerializer(many=False, read_only=True)

#     class Meta:
#         model = Post
#         fields = ('category', 'id', 'title', 'image', 'slug', 'author', 'excerpt', 'content', 'status', 'published')
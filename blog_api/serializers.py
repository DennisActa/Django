from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

class PostSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
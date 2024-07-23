from rest_framework import serializers
from blog.models import Post
from user.models import User


class PostSerializer(serializers.ModelSerializer):
    """Convert Post models to json"""
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Convert User models to json"""
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

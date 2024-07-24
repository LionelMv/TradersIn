from rest_framework import serializers
from blog.models import Post
from user.models import User, Profile


class PostSerializer(serializers.ModelSerializer):
    """Convert Post models to json"""
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'date_posted', 'likes']

    def update(self, instance, validated_data):
        """Remove likes in POST request"""
        validated_data.pop('likes', None)
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Convert User models to json"""
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class ProfileSerializer(serializers.ModelSerializer):
    """Convert Profile models to json"""
    class Meta:
        model = Profile
        fields = "__all__"

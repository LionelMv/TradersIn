from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly, IsAdminOrSelf
from blog.models import Post
from user.models import User
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    """Json representation of all posts"""
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Post author is logged in user"""
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Json representation of a single post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]


class UserList(generics.ListCreateAPIView):
    """Json representation of all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Json representation of a single user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]

    def destroy(self, request, *args, **kwargs):
        """Disallow DELETE method by raising a 403 Forbidden error"""
        return Response(
            {'detail': 'Method "DELETE" not allowed.'},
            status=status.HTTP_403_FORBIDDEN
            )

from django.urls import path
from .views import (
    PostList,
    PostDetail,
    UserList,
    UserDetail,
    ProfileList,
    ProfileDetail,
    ProfileFollowers,
    ProfileFollowing
)

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path("profiles/", ProfileList.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", ProfileDetail.as_view(), name="profile-detail"),
    path("profiles/<int:pk>/followers/", ProfileFollowers.as_view(), name="profile-followers"),
    path("profiles/<int:pk>/following/", ProfileFollowing.as_view(), name="profile-following"),
]

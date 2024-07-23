from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("update_user/", views.update_user, name="update_user"),
    path('follow/<int:pk>/', views.toggle_follow_user, {'action': 'follow'}, name='follow_user'),
    path('unfollow/<int:pk>/', views.toggle_follow_user, {'action': 'unfollow'}, name='unfollow_user'),
]

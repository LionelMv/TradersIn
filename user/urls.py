from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("update_user/", views.update_user, name="update_user"),
]

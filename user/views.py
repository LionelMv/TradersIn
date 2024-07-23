from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from blog.models import Post


def redirect_authenticated_user(view_func):
    """Redirect authenticated user to home page."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect("blog:home")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@redirect_authenticated_user
def register_user(request):
    """Register user page."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,
                             "Your account has been created. Welcome!")
            return redirect("blog:home")
    else:
        form = SignUpForm()

    context = {
        "title": "SignUp",
        "form": form
    }
    return render(request, "user/register.html", context)


@redirect_authenticated_user
def login_user(request):
    """Login user page."""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            next_url = request.GET.get('next', 'blog:home')
            return redirect(next_url)
        else:
            messages.error(request,
                           "Invalid username or password. Please try again.")
    return render(request, "user/login.html", {"title": "Login"})


@login_required
def logout_user(request):
    """Logout user page."""
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("blog:home")


@login_required
def profile(request, pk):
    """Profile page."""
    profile = get_object_or_404(Profile, user_id=pk)

    if request.method == "POST":
        # Get logged in user profile
        current_user_profile = request.user.profile
        action = request.POST.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        else:
            current_user_profile.follows.remove(profile)

        # Save the profile
        current_user_profile.save()

    posts = Post.objects.filter(author_id=pk).order_by("-date_posted")
    context = {
        "title": "Profile",
        "profile": profile,
        "posts": posts,
        "followers_count": profile.followed_by.count(),
        "following_count": profile.follows.count()
    }
    return render(request, "user/profile.html", context)


@login_required
def toggle_follow_user(request, pk, action):
    """Follow or unfollow a user based on the action parameter."""
    profile = get_object_or_404(Profile, user_id=pk)
    current_user_profile = request.user.profile

    if action == 'follow':
        current_user_profile.follows.add(profile)
    elif action == 'unfollow':
        current_user_profile.follows.remove(profile)

    current_user_profile.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def update_user(request):
    """Update user profile."""
    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
            )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if user_form.is_valid() and p_form.is_valid():
            user_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("user:profile", pk=request.user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "title": "Update Profile",
        "user_form": user_form,
        "p_form": p_form
    }
    return render(request, "user/update_user.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfilePictureForm
from functools import wraps
from .models import Profile
from blog.models import Post


def redirect_authenticated_user(view_func):
    """Redirect authenticated user to home page."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,
                             "Logout current user to access this page!")
            return redirect("blog:home")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@redirect_authenticated_user
def register_user(request):
    """Register user page."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Login user
            user = authenticate(username=username, password=password)
            login(request, user)

            # create profile for user
            # profile = Profile.objects.create(user=user)
            messages.success(request,
                             f"Your account has been created. \
                             Welcome!.")
            # redirect to home page after registration
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
            # Get the 'next' parameter or default to 'blog:home'
            next_url = request.GET.get('next', 'blog:home')
            # Redirect to the next URL
            return redirect(next_url)
        else:
            messages.info(request, "Error logging in. Try Again...")
            return redirect("user:login")
    context = {
        "title": "Login"
    }
    return render(request, "user/login.html", context)


@login_required
def logout_user(request):
    """Logout user page."""
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect("blog:home")


@login_required
def profile(request, pk):
    """User profile page."""
    profile = get_object_or_404(Profile, user_id=pk)
    posts = Post.objects.filter(author_id=pk).order_by("-date_posted")

    if request.method == "POST":
        # Get current user
        current_user_profile = request.user.profile
        # Check if user follow/unfollow
        action = request.POST["follow"]
        # Add or remove follow
        if action == "unfollow":
            current_user_profile.follows.remove(profile)
        else:
            current_user_profile.follows.add(profile)
        # Save profile
        current_user_profile.save()
        # Redirect to profile
        return redirect("user:profile", pk=profile.user.id)

    context = {
        "title": "Profile",
        "profile": profile,
        "posts": posts
    }
    return render(request, "user/profile.html", context)


@login_required
def update_user(request):
    """Update user profile page."""
    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
            )
        pic_form = ProfilePictureForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if user_form.is_valid() and pic_form.is_valid():
            user_form.save()
            pic_form.save()
            # login(request, request.user)
            messages.success(request, "Your account has been updated!")
            return redirect("user:profile", pk=request.user.id)

    else:
        user_form = UserUpdateForm(instance=request.user)
        pic_form = ProfilePictureForm(instance=request.user.profile)

    context = {
        "title": "Update Profile",
        "user_form": user_form,
        "pic_form": pic_form
    }

    return render(request, "user/update_user.html", context)

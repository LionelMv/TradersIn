from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from functools import wraps


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

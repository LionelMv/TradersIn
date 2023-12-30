from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile


def register(request):
    """Register user page."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create profile for user
            profile = Profile.objects.create(user=user)
            messages.success(request,
                             f"Your account has been created. \
                             You can now login.")
            return redirect("login")
    else:
        form = UserRegisterForm()

    context = {
        "title": "SignUp",
        "form": form
    }
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    return render(request, "users/profile.html", {"title": "Profile"})

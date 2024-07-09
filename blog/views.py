from django.shortcuts import render
from .models import Post


def home(request):
    """Home page route."""
    context = {
        "title": "Home",
        "posts": Post.objects.all().order_by("-date_posted"),
    }
    return render(request, "blog/home.html", context)
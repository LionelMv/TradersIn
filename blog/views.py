from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# def home(request):
#     """Home page route."""
#     context = {
#         "title": "Home",
#         "posts": Post.objects.all().order_by("-date_posted"),
#     }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    # paginate_by = 5


class PostDetailView(DetailView):
    model = Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post


# def home(request):
#     """Home page route."""
#     context = {
#         "title": "Home",
#         "posts": Post.objects.all().order_by("-date_posted"),
#     }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    """Home page view."""
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    # paginate_by = 5


class PostDetailView(DetailView):
    """Post detail view."""
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Post create view."""
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """Override form_valid method."""
        form.instance.author = self.request.user
        return super().form_valid(form)

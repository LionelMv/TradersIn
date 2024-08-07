from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Post update view."""
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """Override form_valid method."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Override test_func method."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Post delete view."""
    model = Post
    success_url = "/"

    def test_func(self):
        """Override test_func method."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def post_like(request, pk):
    """Post like view."""
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get("HTTP_REFERER"))

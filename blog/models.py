from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """Creates the post fields.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    def total_likes(self):
        """Returns the total likes of the post.
        """
        return self.likes.count()

    def __str__(self) -> str:
        """String representation of the class Post.
        """
        return self.title

    def get_absolute_url(self):
        """Returns the absolute url of the post.
        """
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

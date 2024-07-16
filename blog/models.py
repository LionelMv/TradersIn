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

    def __str__(self) -> str:
        """String representation of the class Post.
        """
        return self.title

    def get_absolute_url(self):
        """Returns the absolute url of the post.
        """
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

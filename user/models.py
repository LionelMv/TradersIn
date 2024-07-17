from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False,
                                     blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

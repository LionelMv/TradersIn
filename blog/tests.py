from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Test Content')
        self.assertEqual(self.post.author.username, 'testuser')


class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')


class UserAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login(self):
        response = self.client.post(reverse('user:login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_logout(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

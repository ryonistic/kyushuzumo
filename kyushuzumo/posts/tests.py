"""This test creates a sample user and then uses
it to create a blog post in order to check if the post
created has the expected fields or not."""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    """This test function creates a sample user and then
    saves it, after that it creates a post with the author
    set to the user we created. Then saves it too."""
    @classmethod
    def setUpTestData(cls):
        #Create a User
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        #Create a post
        test_post = Post.objects.create(
        author=testuser1, title='Blog Title', body='Body content...')
        test_post.save()

    def test_blog_content(self):
        """This is a test to check whether the
        blog post created above actually saves info
        properly or not."""
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body content...')

"""Post mode has an overriden save method that adds a slug to the field 
and makes sure that the images are less than 700x700 in size. There is also
a get_absolute_url method to make sure that the url per instance is taken care of."""
from PIL import Image
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    """slugs are unique, author sets to null on on_delete"""
    title = models.CharField(max_length=150)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, unique=True)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')

    def save(self, *args, **kwargs):
        """creating a SlugField for each instance
        by overriding the save method"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # each image file must be sized down to save space
        image = Image.open(self.image.path)
        if image.height > 700 or image.width > 700:
            output_size = (700, 700)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def get_absolute_url(self):
        return f"/postdetail/{self.slug}/"

    def __str__(self):
        return str(f'{self.title} by {self.author}')

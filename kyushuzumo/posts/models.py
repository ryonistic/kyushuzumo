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

class Pro(models.Model):
    SUMO_RANKS = (
            ('JONOKUCHI', 'JONOKUCHI'),
            ('JONIDAN', 'JONIDAN'),
            ('SANDANME', 'SANDANME'),
            ('MAKUSHITA', 'MAKUSHITA'),
            ('JURYO', 'JURYO'),
            ('MAEGASHIRA', 'MAEGASHIRA'),
            ('MAEGASHIRA', 'MAEGASHIRA'),
            ('KOMUSUBI', 'KOMUSUBI'),
            ('SEKIWAKE', 'SEKIWAKE'),
            ('OZEKI', 'OZEKI'),
            ('YOKOZUNA', 'YOKOZUNA'),
            )
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=500)
    height = models.PositiveBigIntegerField(default=170)
    weight = models.PositiveBigIntegerField(default=90)
    wins = models.PositiveBigIntegerField(default=0)
    losses = models.PositiveBigIntegerField(default=0)
    no_contest = models.PositiveBigIntegerField(default=0)
    rank = models.CharField(choices = SUMO_RANKS, max_length=255, null=True, blank=True)
    championships = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='pros/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # each image file must be sized down to save space
        image = Image.open(self.image.path)
        if image.height > 700 or image.width > 700:
            output_size = (700, 700)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

class Admission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    experience_level = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Continent(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Continent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=128, unique=True)
    continent = models.ForeignKey(Continent)
    short_description = models.CharField(max_length=1280)
    description = models.CharField(max_length=1280)
    ingredients = models.CharField(max_length=1280)
    steps = models.CharField(max_length=1280)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe_name


class Review(models.Model):
    recipe_name = models.ForeignKey(Recipe)
    review_text = models.CharField(max_length=1280)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text


class Favourites(models.Model):
    account = models.ForeignKey(User)
    recipe_name = models.ForeignKey(Recipe)

    class Meta:
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return self.account

    
""" Laimonous reported an error here for log in creation, so User class commented
class User(models.Model):
    name = models.CharField(max_length=128)
    account = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=16)
    # I changed the field type of favourites to URL since I thought it should save a set of recipes
    favourites = models.URLField(max_length=256)
"""


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username


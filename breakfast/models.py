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
    text = models.CharField(max_length=12)
    recipe_name = models.CharField(max_length=128, unique=True)
    continent = models.ForeignKey(Continent)
    short_description = models.CharField(max_length=1280)
    description = models.CharField(max_length=1280)
    ingredients = models.CharField(max_length=1280)
    steps = models.CharField(max_length=1280)
    keywords = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='recipe_images',null=True,blank=True)
    slug = models.SlugField(unique=True)
    continent_slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipe_name)
        self.continent_slug = slugify(self.continent)
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


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
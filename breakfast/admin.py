from django.contrib import admin
from breakfast.models import Continent, Recipe, Review, Favourites

admin.site.register(Continent)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Favourites)

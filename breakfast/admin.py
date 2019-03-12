from django.contrib import admin
from breakfast.models import Continent, Recipe, Review, Favourites

class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'continent', 'short_description', 'description', 'ingredients', 'steps', 'views', 'likes', 'image')

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review)
admin.site.register(Favourites)

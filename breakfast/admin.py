from django.contrib import admin
from breakfast.models import Continent, Recipe, Review, Favourites, UserProfile

class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'continent', 'short_description', 'views', 'likes')

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review)
admin.site.register(Favourites)
admin.site.register(UserProfile)
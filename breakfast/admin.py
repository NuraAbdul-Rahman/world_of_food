from django.contrib import admin
from breakfast.models import Continent, Recipe, Review, Favourites

class ContinentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Favourites)

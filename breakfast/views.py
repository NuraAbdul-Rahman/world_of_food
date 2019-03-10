
from django.shortcuts import render
from breakfast.models import Continent
from breakfast.models import Recipe



# Create your views here.
def home(request):
    return render(request, 'breakfast/home.html', {})
   
def about(request):
    return render(request, 'breakfast/about.html', {})

def contact_us(request):
    return render(request, 'breakfast/contact_us.html', {})

def sign_in(request):
    return render(request, 'breakfast/sign_in.html', {})

def sign_up(request):
    return render(request, 'breakfast/sign_up.html', {})

def my_account(request):
    return render(request, 'breakfast/my_account.html', {})

def continent_page(request, continent_name_slug):
    
    context_dict = {}

    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        recipe = Recipe.objects.filter(continent=continent)

        context_dict['recipe'] = recipe
        context_dict['continent'] = continent
    except Continent.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipe'] = None

    return render(request, 'breakfast/continent_page.html', context_dict)

def recipe_page(request, recipe_name_slug):

    context_dict = {}

    try:
        recipe = Recipe.object.get(slug=recipe_name_slug)
        continent = Recipe.object.get(continent)
        description = Recipe.object.get(description)
        ingredients = Recipe.object.get(ingredients)

        context_dict['recipe'] = recipe
        context_dict['continent'] = continent
        context_dict['description'] = description
        context_dict['ingredients'] = ingredients
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
        context_dict['continent'] = None
        context_dict['description'] = None
        context_dict['ingredients'] = None
        
    return render(request, 'breakfast/recipe_page.html', context_dict)
   


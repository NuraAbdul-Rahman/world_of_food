from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from breakfast.models import Continent, Recipe, Favourites, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from breakfast.forms import UserForm,UserProfileForm,ContinentForm,RecipeForm
from django.contrib.auth.decorators import login_required
# from registration.backends.simple.views import RegistrationView

def home(request):
    continent_list = Continent.objects.all()
    context_dict = {'continents': continent_list}
    return render(request, 'breakfast/home.html', context_dict)


def about(request):
    return render(request, 'breakfast/about.html', {})


def contact_us(request):
    return render(request, 'breakfast/contact_us.html', {})


def sign_in(request):
    # return render(request, 'breakfast/sign_in.html', {})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Breakfast account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied. Please check your username and password!")

    else:
        return render(request, 'breakfast/login.html', {})


def sign_up(request):
    # return render(request, 'breakfast/sign_up.html', {})
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'breakfast/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")


def my_account(request):
    return render(request, 'breakfast/my_account.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def show_continent(request, continent_name_slug):
    
    context_dict = {}

    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        recipe = Recipe.objects.filter(continent=continent)

        context_dict['recipes'] = recipe
        context_dict['continent'] = continent
    except Continent.DoesNotExist:
        context_dict['continent'] = None
        context_dict['recipes'] = None

    return render(request, 'breakfast/continent.html', context_dict)



def show_recipe(request, recipe_name_slug):

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
        
    return render(request, 'breakfast/recipe.html', context_dict)


def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'breakfast/recipe_page.html', {'form': form})
   


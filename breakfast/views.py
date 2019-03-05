
from django.shortcuts import render
from django.http import HttpResponse
from breakfast.models import Continent


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

def continent_page(request, Continent_name_slug):
    context_dict {}

    try:
        continent = Continent.objects.get[slug=Continent_name_slug]

    return render(request, 'breakfast/continent_page.html', {})

def recipe_page(request):
    return render(request, 'breakfast/recipe_page.html')
   


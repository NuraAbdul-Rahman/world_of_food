from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from breakfast.models import Continent, Recipe, Favourites, Review, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from registration.backends.simple.views import RegistrationView
from breakfast.forms import UserForm,UserProfileForm,ContinentForm,RecipeForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()) )

    last_visit_time = datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")
    
    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

def base(request):
    continent_list = Continent.objects.all()
    context_dict = {'continents': continent_list}
    return render (request, 'breakfast/base.html, context_dict')

def home(request):
    request.session.set_test_cookie()
    continent_list = Continent.objects.all()
    recipe_list = Recipe.objects.order_by('-likes')[:5]
    context_dict = {'continents': continent_list, 'recipes': recipe_list}
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'breakfast/home.html', context_dict)
    return response


def about(request):
    return render(request, 'breakfast/about.html', {})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            messages.info(request,'Thanks for  contacting us!')
            return HttpResponseRedirect(reverse('contact_us'))
    else:
        form = ContactForm()
    return render(request, 'breakfast/contact_us.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request,'Your Breakfast account is disabled.')
                return HttpResponseRedirect(reverse('sign_in'))
        else:
            messages.error(request,'Invalid login details supplied. Please check your username and password!')
            return HttpResponseRedirect(reverse('sign_in'))

    else:
        return render(request, 'breakfast/sign_in.html', {})

@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))




def sign_up(request):
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
            messages.success(request, 'You have sign up successfully!')  

        else:
            messages.error(request,'User already exists, enter new details')
            print(user_form.errors, profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'breakfast/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect('home')
        else:
            print(form.errors)

    context_dict = {'form':form}
    
    return render(request, 'breakfast/profile_registration.html', context_dict)

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

class BreakfastRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

@login_required
def my_account(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('home')
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('my_account', user.username)
        else:
            print(form.errors)
    
    return render(request, 'breakfast/my_account.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})

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



def show_recipe(request, continent_name_slug, recipe_name_slug):

    context_dict = {}

    try:
        recipe = Recipe.objects.filter(slug=recipe_name_slug)
        context_dict['recipe'] = recipe
        
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
        
    return render(request, 'breakfast/recipe.html', context_dict)

@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'breakfast/add_recipe.html', {'form': form})
   
@login_required
def like_recipe(request):
    recipe_id = None
    if request.method == 'GET':
        recipe_id = request.GET['recipe_id']
        likes = 0
        if recipe_id:
            recipe = Recipe.objects.get(id=int(recipe_id))
            if recipe:
                likes = Recipe.likes + 1
                recipe.likes = likes
                recipe.save()
        return HttpResponse(likes)
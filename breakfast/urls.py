
from django.conf.urls import url
from breakfast import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'contact_us', views.contact_us, name='contact_us'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/my_account/$', views.my_account, name='my_account'),
    url(r'^(?P<continent_name_slug>[\w\-]+)/$',
        views.continent_page, 
        name='continent_page'),
    url(r'^(?P<continent_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)',
        views.recipe_page, 
        name='recipe_page'),


]
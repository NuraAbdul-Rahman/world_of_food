
from django.conf.urls import url
from breakfast import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'contact_us', views.contact_us, name='contact_us'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^my_account/(?P<username>[\w\-]+)/$', views.my_account, name='my_account'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^continent/(?P<continent_name_slug>[\w\-]+)/$',
        views.show_continent,
        name='show_continent'),
   
    url(r'^continent/(?P<continent_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)/$',
        views.show_recipe, 
        name='show_recipe'),

    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
]

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from breakfast import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^breakfast/', include('breakfast.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', views.BreakfastRegistrationView.as_view(), name='registration_register'),
    url(r'^search/', include('haystack.urls')),
<<<<<<< HEAD
    # url(r'^like/$', views.like_recipe, name='like_recipe'),
=======
    url(r'^like$', views.like_recipe, name='like_recipe'),
>>>>>>> 3dfa2187a16e1c4078cf76e63f299df980d9ded8
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


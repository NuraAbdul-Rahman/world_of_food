
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
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
    url(r'^reg/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


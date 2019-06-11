from django.conf.urls import url
from django.contrib import admin
from deploytodotaskerapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    # Whenever you go to root path or 'home', application will run the views.home function and render the home.html
]

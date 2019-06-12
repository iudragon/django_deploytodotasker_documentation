from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# To differentiate between two view, we give alias 'auth_views'

from django.conf.urls.static import static
from django.conf import settings
# Above two: That's all we need to do for uploading images

from deploytodotaskerapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    # Whenever you go to root path or 'home', application will run the views.home function and render the home.html
    url(r'^registration/login/$', auth_views.LoginView.as_view(),
        {'template_name': 'registration/login.html'},
        name = 'registration-login'),
    url(r'^registration/sign-out', auth_views.LogoutView.as_view(),
        {'next_page': '/'},
        name = 'registration-sign-out'),

    # Here we do not use views from deploytodotaskerapp, instead we use auth_views which is an alias of authentication library from django
    url(r'^registration/sign-up', views.registration_sign_up,
        name = 'registration-sign-up'),
    url(r'^registration/$', views.registration_home, name = 'registration-home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

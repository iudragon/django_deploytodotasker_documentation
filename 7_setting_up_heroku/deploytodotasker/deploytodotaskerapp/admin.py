from django.contrib import admin

from deploytodotaskerapp.models import Registration

# We imported Registration here and we add that Registration object into the admin site.

admin.site.register(Registration)

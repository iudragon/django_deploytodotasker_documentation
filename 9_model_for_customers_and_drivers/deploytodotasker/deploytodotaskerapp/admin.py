from django.contrib import admin

from deploytodotaskerapp.models import Registration, Customer, Driver

# We imported Registration here and we add that Registration object into the admin site.

admin.site.register(Registration)
admin.site.register(Customer)
admin.site.register(Driver)

from django import forms
from django.contrib.auth.models import User
from deploytodotaskerapp.models import Registration



# We are going to create two forms, one for Registration owner for which we are going to use User object and we will add fiels like username, password... Similary we create another form for Registration itself
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ("name", "phone", "address", "logo")

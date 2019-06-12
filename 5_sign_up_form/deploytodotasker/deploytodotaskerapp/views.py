from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from deploytodotaskerapp.forms import UserForm, RegistrationForm


# **** THIS IS BEFORE YOU IMPORT AND USE login_required
# Click Sign Out and check logs in terminal [command prompt], you will see registration/sign-out

# *Right now anyone can go to localhost:8000/registration/ page. We want only authenticated user to be able to access that page.*
# **** THIS IS BEFORE YOU IMPORT AND USE login_required


def home(request):
    return redirect(registration_home)
    # To be able to use redirect, we need to import it. redirect is a django Function

# Before we go to registration page we need to check authentication of user. If user is authenticated we will allow them to go to registration/home.html home page otherwise we will redirect user to registration/login.html
@login_required(login_url='registration/login/')
def registration_home(request):
    return render(request, 'registration/home.html', {})

def registration_sign_up(request):
    user_form = UserForm()
    registration_form = RegistrationForm()
    # We are going to create this two forms and pass this to Front End
    return render(request, 'registration/sign_up.html', {
        "user_form": user_form,
        "registration_form": registration_form
        # Basically we upgraded variable names "user-form" and "registration_form" We can name it whatever we want but we have to make sure those variables names are linked.
        # To be able to use these variable names in Front End open sign_up.html
    })

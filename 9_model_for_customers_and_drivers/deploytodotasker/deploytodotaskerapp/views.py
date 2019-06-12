from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from deploytodotaskerapp.forms import UserForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Because we are going to use user model of django


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

    # When user click on submit button, it goes to this block
    if request.method == "POST":
        # We get data from user and registration form including images
        user_form = UserForm(request.POST)
        registration_form = RegistrationForm(request.POST, request.FILES)
        # request.FILES because inside of registration_form we allow user to upload the logo

        if user_form.is_valid() and registration_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            # Give cleaned data and transform it to python type

            new_registration = registration_form.save(commit=False)
            # commit=False: Create new registration object but just in memory
            new_registration.user = new_user
            # user of that registration is the new_user
            new_registration.save()
            # Now it goes to database

            # Once we get the new user and the new registration, we call the login function and we are going to pass the username and password and then we redirect to registration home page.

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(registration_home)

    return render(request, 'registration/sign_up.html', {
        "user_form": user_form,
        "registration_form": registration_form
        # Basically we upgraded variable names "user-form" and "registration_form" We can name it whatever we want but we have to make sure those variables names are linked.
        # To be able to use these variable names in Front End open sign_up.html
    })

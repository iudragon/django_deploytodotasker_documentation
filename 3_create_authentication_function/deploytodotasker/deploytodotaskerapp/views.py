from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    return render(request, 'registration/home.html')

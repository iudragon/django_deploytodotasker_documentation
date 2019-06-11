## Create virtual environment for our python app

Virtual environment is the tool to keep the dependency required by different projects in a separate place.

*Project A depends on Version 1 but Project B depends on Version 2, so the virtual environment helps us to manage all this easily.*

## Create virtual environment

`virtualenv deploytodoenv/deploytodotasker`

**Output:** New folder named deploytodoenv and inside it deploytodotasker.


## Activate virtual environment

`Go to Scripts and enter activate.`

**Output:** You will see (deploytodotasker) like this in parenthesis.


## Install Django for our virtual environment

*pip is a python package manager to help you to install python dependencies*

Check if django is installed by

`pip freeze`


## Create Django project

`django-admin startproject deploytodotasker`

**Output:** New folder name deploytodotasker (contains deploytodotasker folder and manage.py files)

Go to deploytodotasker project

`cd deploytodotasker`

Start server

`python manage.py runserver`

Open web browser, and go to 127.0.0.1:8000 or localhost:8000
If you see a Django page, everything is working fine.

Stop runserver

`Ctrl + C`


## Create git repository

Initialize empty git repository

'git init'

Open atom editor (or any other) and drag your deploytodotasker project folder in it.

Inside deploytodotasker project folder create `.gitignore` file

`__pycache__/`

`db.sqlite3`

`*.pyc`

Add to git

`git add .`

Commit to git

`git commit -m "Git first commit"`


## Create app

We can have multiple apps in Django. Here, we create one app called deploytodotaskerapp

`python manage.py startapp deploytodotaskerapp`

**Output:** You will see deploytodotaskerapp inside deploytodotaskerapp project folder

As we create new app, we need to tell django about this.

Open deploytodotasker then settings

Inside `INSTALLED_APPS` add at the bottom

`'deploytodotaskerapp',`


## Create home page

Under deploytodotaskerapp then open views.py

Create function `[refer code]`

views.py is just like controller in MVC model. it handles all the business logic and getting, processing data here. Then it will pass the result to Front End.

We want to redirect to home page.

Under deploytodotasker, open urls.py `[refer code]`

Under deploytodotaskerapp, create new folder 'templates' and create new file under 'templates' named 'home.html' `[refer code]`

Run server

`python manage.py runserver`

**Output:** Hello Python!

Now when you first go to localhost:8000

It first goes to deploytodotasker/urls.py and it looks for `urlpatterns` and then it comes to conclusion that we want to run `views.home` function.

Then it goes to deploytodotaskerapp/views.py and finds the function named `home`

And inside the function `home`, it renders the `home.html`

Then it goes to `home.html` and renders exactly what it sees in the code.

This is the process of urls.py, views.py, home.html

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


## Create Django dashboard

Migrate

`python manage.py migrate`

Create super user

`python manage.py createsuperuser`

Username: admin

Email addess: admin@example.com

Password: 12345678

Run server

`python manage.py runserver`

In web browser go to localhost:8000/admin and enter username and password you created. Now you are into Django dashboard.


## Adding Bootstrap

Download Bootstrap

Under deploytodotaskerapp create new folder `static` and under it another folder `css`

Under `static` folder create another folder `img` and `font` and `js`

From Bootstrap downloaded folder, if you have fonts then move to `font` folder we just created or if you don't have skip this step.

Move bootstrap.min.css to our static/css folder.

Move bootstrap.min.js to our static/js folder.

We need to implement Bootstrap on our page.

Open `home.html` `[refer code]`

Under `css` folder create new file `style.css` `[refer code]`


## Create Authentication Function

We want to create login and sign out process.

Open deploytodotasker/urls.py `[refer code]`

Under deploytodotaskerapp/templates create new folder `registration` and inside it new file `login.html` `[refer code]`

Open deploytodotasker/settings.py
Add `LOGIN_REDIRECT_URL ='/'` or
`[refer code]`

Go to web browser and enter localhost:8000/registration/login

You will see login form generated by django.

Now enter your username and password you created [super user]
Username: admin
Password: 12345678

You will be redirected to home page upon clicking login.

Under templates/registration create new file `home.html` `[refer code]`

Open urls.py `[refer code]`

Open views.py `[refer code]`

Delete home.html folder under templates [the older home.html]

Go to localhost:8000/registration

You will see login page. Type username and password and then you will be redirected to registration/home home page.


## Create Model for registration

Previously we create login and sign out function for user and we tested it with super user account.

Now we want registration owners to create account, so we are going to create model for registration.

There are two objects in our scenario: Registration owner and registration itself.

For registration owners we are going to use Users object provided by django.

Our task is to create model for registration and that is the custom model.

Under deploytodotaskerapp open models.py `[refer code]`

Then in terminal

`pip install pillow`

*Every time a model is created or changed, run this two command*

`python manage.py makemigrations`

`python manage.py migrate`

Open deploytodotasker/urls.py `[refer code]`

Open deploytodotaskerapp/views.py `[refer code]`

Under templates, create new file 'sign_up.html' `[refer code]`

Go to localhost:8000/registration/sign-up

Now, again we understood how urls.py, views.py, sign_up.html works together.

Right now, we have nothing on Sign Up page. We need to create forms for registration.


## Sign Up Form

Under deploytodotaskerapp create new file `forms.py` `[refer code]`

Open deploytodotaskerapp/views.py `[refer code]`

Open registration/sign_up.html `[refer code]`

Go to localhost:8000/registration/sign-up

You will see forms with UserForm fields and RegistrationForm fields

Sending data won't work at this moment. We have to tell django what to do when data is submitted.

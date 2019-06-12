## Create virtual environment

Virtual environment is the tool to keep the dependency required by different projects in a separate place.

*Project A depends on Version 1 but Project B depends on Version 2, so the virtual environment helps us to manage all this easily.*

In terminal [command prompt] for Windows user:

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

**Output:** You will see deploytodotaskerapp inside deploytodotasker project folder

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


## Send Data using Form

Open deploytodotaskerapp/forms.py `[refer code]`

Open deploytodotaskerapp/views.py `[refer code]`

We are going to upload images to our server, we need to store them.

Open deploytodotasker/settings.py `[refer code]`

Open sign_up.html `[refer code]`

Open deploytodotasker/urls.py `[refer code]`

Open deploytodotaskerapp/admin.py `[refer code]`

Go to localhost:8000/registration/sign-up and fill the form and press sign up button.

You will be redirected to home page.

To confirm you are logged in. Go to localhost:8000/admin and enter your super user name and password.

In Users, you will see the newly created username and other details you just filled out.


## Setting Heroku [For now, later we will use Digital Ocean]

In terminal, make sure you are in deploytodotasker project folder.

`heroku login`

Login to heroku

`heroku create`

Under deploytodotasker project folder, create new file `runtime.txt` `[refer code]`

Because we need to tell heroku what needs to be installed.

In terminal

`pip install gunicorn`

We need to tell heroku what we installed.

Under deploytodotasker project folder, create new file `requirements.txt` `[refer code]`

Copy all the dependencies you installed to requirements.txt

Do `pip freeze` to view all the dependencies.

Under deploytodotasker project folder, create new file `Procfile` [with no extension] `[refer code]`

In terminal `pip install whitenoise` [for serving static files]

Open requirements.txt, paste the whitenoise dependency `[refer code]`

Open settings.py `[refer code]`

Open wsgi.py `[refer code]`

Now we are going to configure database so it works with heroku

In terminal, `pip install dj-database-url`

Copy the dependency and paste this in requirements.txt `[refer code]`

Add package `psycopg2` and `psycopg2-binary`

NOTE: we add the above two dependency in our requirements.txt but do NOT install it using pip.

We do not install on local. Because our local database is sqlite but when we upload our app to heroku, we need to use postgres. Because heroku supports postgres database.

Open settings.py `[refer code]`

In terminal

`git add .`

`git commit -m "Deploy to heroku"`

`git push heroku master`

`heroku run python manage.py migrate`

Migrates all database structure from local to Heroku [not data]

`heroku run python manage.py createsuperuser`

Username: admin

Email: admin@example.com

Password: 12345678

`heroku open`

Web browser will open. You will see login form.

Go to /admin of your heroku site. You will see django dashboard.

Note: Clicking on registration in django dashboard will display error for now.


## Facebook Authentication

Go to developers.facebook.com

Create new app

Select website

Create new Facebook App Id

In facebook dashboard, go to settings

Add platform

Select website

Enter url: http://localhost:8000

Save changes  

*In our app, customer and driver will sign in using their facebook account. Then they will send their facebook token to our server to process*

To be able to work with RESTful api from facebook we need to install django-rest-framework-social-oauth2

In terminal, while keeping your virtual environment activated as before and inside deploytodotasker project folder install:

`pip install django-rest-framework-social-oauth2`

Add dependency to requirements.txt `[refer code]`

Open settings.py `[refer code]`

We will refer code from https://github.com/RealmTeam/django-rest-framework-social-oauth2

Open urls.py `[refer code]`

In terminal

`python manage.py migrate`

`python manage.py runserver`

Go to localhost:8000/admin

In django dashboard, you will see DJANGO OAUTH TOOLKIT and PYTHON SOCIAL AUTH

We are going to create application for our DJANGO OAUTH TOOLKIT.

Click on application

Add Application

NOTE: Client Id and Client Secret should NEVER be changed.

Save those carefully.

Enter user as 1 [admin i.e superuser]

Keep redirect uris  blank

Client type: Confidential

Authorization grant type should be resource owner password based

Set name as whatever you want

Click save

*As of now, we installed django rest framework social oauth. Now we will use facebook api to create new users*

Suppose we have an android app [which we are going to create soon with documentation] with facebook login button.

As we click on facebook login, the request will be sent to facebook to authorize it.

Once facebook authorize it, it will send facebook token back to the android app.

Then the android app with send the facebook token along with some parameters to this api: localhost:8000/api/social/convert-token

Once we get the request above, django rest framework social oauth will create new user and access token into the database.

And then it sends access token and refresh token back to the android app

Every time, android app user will request something from server, android app needs to send the access token as well.

We do not have android app at this moment. So we will use POSTMAN

Open POSTMAN

POST, url: localhost:8000/api/social/convert-token

Params:-

Key: grant_type | value: convert_token

Key: client_id | value: paste from django dashboard application client id

key: client_secret | value: paste from django dashboard application client secret

key: backend | value: facebook

key: token | value: paste from developers.facebook.com/tools/accesstoken [use User Token]

Click send

You will get access token and refresh token plus other information.

Now, check django admin dashboard for new user. You will find one with facebook name of that user. But you won't find the email of the user.

To get the email addess:

Go to developers.facebook.com/tools/explorer

Select your application

Click get token --> get user access token and tick the email and click on get access token button.

Copy the access token.

Paste it in the POSTMAN token value.

Click send.

Check django admin dashboard, you will find email address of that facebook user.

In POSTMAN on another tab:-

POST, url: localhost:8000/api/social/revoke-token

Params:-

key: client_id | value: paste from django dashboard application client id

key: client_secret | value: paste from django dashboard application client secret

key: token | value: *Token here is the access token you will find in django admin dashboard, under django oauth toolkit --> access token. Copy an access token from there and paste it as value in POSTMAN*

Click send.

You will not see anything in POSTMAN.

Go to django admin dashboard access token. You will see that access token previously copied and pasted in token value in POSTMAN is now removed.

*Once you sign out, the access token needs to be deleted from the server. This how it works for normal user. As you login again, new access token will be created.*


## Model for Customer and Driver

Open models.py `[refer code]`

Open admin.py `[refer code]`

In terminal

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

*Previously we learn how to use django rest framework social oauth for login, sign up and sign out process*

But there is no way to customize our login process. When someone sign up, we need to know whether they are customer or driver so that we can set them in the correspondent table in the database. We could that using pipeline.

Open settings.py `[refer code]`

Under deploytodotaskerapp, create new file `social_auth_pipeline.py` `[refer code]`

Open POSTMAN

POST, url: localhost:8000/api/social/convert-token

Params:-

Key: grant_type | value: convert_token

Key: client_id | value: paste from django dashboard application client id

key: client_secret | value: paste from django dashboard application client secret

key: backend | value: facebook

key: token | value: paste from developers.facebook.com/tools/accesstoken [use User Token]

key: user_type | value: driver [later try with different value, that will be then be associated with customer model in django admin dashboard]

Click send

Now check in django admin dashboard you will see new driver.

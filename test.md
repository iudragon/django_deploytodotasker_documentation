# Create virtual environment for our python app
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

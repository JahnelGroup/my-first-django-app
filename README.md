# My First Django App

Django has great documentation and a guide to [getting started](https://docs.djangoproject.com/en/2.2/intro/) with your first app. You can also watch this excellent video by Justin Mitchel: [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4).

## Setup Python and Django

Follow this guide on [managing multiple python versions](https://realpython.com/intro-to-pyenv/) to install [pyenv](https://github.com/pyenv/pyenv#installation). Once you have *pyenv* installed you can install any version of python and create virtual environments.

Install **Python 3.7.3**, configure a virtual environment, active it with the local command, upgrade pip, and then install **Django 2.2.2**.

```bash
$ pyenv install -v 3.7.3
$ pyenv virtualenv 3.7.3 my-first-django-app
$ pyenv local my-first-django-app
(my-first-django-app) [my-first-django-app]$ python -V
Python 3.7.3
(my-first-django-app) [my-first-django-app]$ pip install --upgrade pip
(my-first-django-app) [my-first-django-app]$ pip install Django==2.2.2
```

Now your pip freeze should look something like this:

```bash
(my-first-django-app) [my-first-django-app]$ pip freeze
Django==2.2.2
pytz==2019.1
sqlparse==0.3.0
```

## Intialize the Project and Run Server

Use the [django-admin](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-and-manage-py) command with the [startproject](https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject) switch to initialize your Django project.

```bash
(my-first-django-app) [my-first-django-app]$ mkdir src
(my-first-django-app) [my-first-django-app]$ django-admin startproject app src
(my-first-django-app) [my-first-django-app]$ ls src
app  manage.py
```

Run the server:

```bash
(my-first-django-app) [my-first-django-app]$ python src/manage.py runserver
...
Django version 2.2.2, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Navigate to http://localhost:8000 to see the congratulations page!

## Run Database Migrations

Use manage.py with the [showmigrations](https://docs.djangoproject.com/en/2.2/ref/django-admin/#showmigrations) and [migrate](https://docs.djangoproject.com/en/2.2/ref/django-admin/#migrate) switches to list the available migrations and then run them.

```bash
$ python src/manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```

```bash
$ python src/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

## Admin Page / Super User

Use manage.py with the [createsuperuser](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser) switch to create your super user account.

```bash
(my-first-django-app) [my-first-django-app]$ python src/manage.py createsuperuser --username superadmin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

Have your server running then navigate to http://localhost:8000/admin to and login with your super user account.

## Create a 'TODO' App

Use manage.py with the [createsuperuser](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser) switch to create your super user account.
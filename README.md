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

## Initialize the Project and Run Server

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

Use manage.py with the [startapp](https://docs.djangoproject.com/en/2.2/ref/django-admin/#startapp) switch to create the seed of [src/todo](./src/todo):

```bash
$ cd src
$ python manage.py startapp todo
```

### Views, Model and Admin

Create the Todo model, views and register it with the admin app.

* Update [src/todo/models.py](./src/todo/models.py) with TODO models.
* Update [src/todo/views.py](./src/todo/views.py) with controller functions.
* Update [src/todo/admin.py](./src/todo/admin.py) to register admin functionality from /admin.

### Activate Todo App in Django

Integrate the Todo app with Django:

* Update [src/app/settings.py](./src/app/settings.py) to add TodoConfig to INSTALLED_APPS. 
* Create [src/todo/urls.py](./src/todo/urls.py) then add routes to the controller.
* Update [src/app/urls.py](./src/app/urls.py) to include the todo urls.

### Django Templates

Create Django [templates](./src/todo/templates) to display your Todo model.

### Database Migrations

Create migrations for the Todo model and run them:

```bash
$ python src/manage.py makemigrations
Migrations for 'todo':
  todo/migrations/0001_initial.py
    - Create model Todo
$ python src/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo
Running migrations:
  Applying todo.0001_initial... OK
```

Now you can login to the [admin](http://localhost:8000/admin) and perform CRUD operations on Todo's. 

### Django Python Shell

Django's python shell is another option to manage your application, launch it with `python src/manage.py shell`.

```bash
$ python manage.py shell
Python 3.7.3 (default, Jun  5 2019, 21:07:12) 
[GCC 8.3.1 20190223 (Red Hat 8.3.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from todo.models import Todo
>>> Todo.objects.all()
<QuerySet [<Todo: Todo object (1)>]>
>>> Todo.objects.create(title='Title 2', description='Description 2')
<Todo: Todo object (2)>
>>> Todo.objects.all()
<QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>]>
```
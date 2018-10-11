# Employee Service API
## About
This is a simple Employee service API that I created as an example for learning Django REST Framework.
## Goal
The goal of this project is teach Django REST framework on novice programmers.
## Features
With this API;
- You can create and view a employee
## Technology stack
Tools used during the development of this API are;
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [SQLite](https://www.sqlite.org/) - this is a database server
## Requirements
- Use Python 3.x.x+
- Use Django 2.x.x+

## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ cd drf_basic
    $ virtualenv --python=python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```
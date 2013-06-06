djvasa
======

(Dj)ango - (Va)grant - (Sa)ltStack

This is currently under development, the general idea here is to be able to quickly spin up new Django projects
quickly and get to work.  I'll be utilizing Vagrant to create a virtual environment and will be adding pieces to
also setup other tools needed, like a database.

In it's current state, djvasa will create a functional django project.  Next on the list is the Vagrant bits and as
soon as I get that wrapped up I'll start working on scripts for things like MySQL or Postgres.

Once I get the Vagrant bits added, and anything else that I think is missing, I'll package it up and put it on pypi,
but for now if you want to use it, you can do the following:

    >> pip install git+git://github.com/cgallemore/djvasa.git
    >> djvasa
    What's the name of your project? foobar
    What's your full name? Chad Gallemore
    What's your email? cgallemore@gmail.com
    >> cd foobar/
    >> virtualenv venv --distribute
    >> . venv/bin/activate
    >> pip install -r requirements.pip
    >> python manage.py syncdb
    >> python manage.py runserver
    http://localhost:8000/admin/

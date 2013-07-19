======
djvasa
======

.. image:: https://badge.fury.io/py/djvasa.png
    :target: http://badge.fury.io/py/djvasa

.. image:: https://travis-ci.org/cgallemore/djvasa.png?branch=master
    :target: https://travis-ci.org/cgallemore/djvasa

.. image:: https://pypip.in/d/djvasa/badge.png
    :target: https://crate.io/packages/djvasa/

(Dj)ango - (Va)grant - (Sa)ltStack

In an effort to learn about Vagrant and SaltStack I had the idea to create a tool to help me initialize Django
projects more efficiently, this is the result.  Djvasa is a command line tool to help you rapidly create a Django
project for use with Vagrant.  In addition, the Vagrant environment can be provisioned with certain tools typical
to a Django project ready for use.  The provisioning is handled with SaltStack.

The following guide assumes you already have Vagrant and VirtualBox installed and that you have the salty-vagrant
plugin installed.  If you have Vagrant and VirtualBox already, but need the plugin, you can install like so:

::

    >> vagrant plugin install vagrant-salt

Quick Start
-----------

::

    >> pip install djvasa
    >> djvasa --postgres
    What's the name of your project? foobar
    What's your full name? Chad Gallemore
    What's your email? cgallemore@gmail.com

    >> cd foobar
    >> vagrant up
    >> vagrant ssh
    >> . .virtualenvs/{{project_name}}/bin/activate && cd /vagrant
    >> python manage.py syncdb
    >> python manage.py runserver 0.0.0.0:8000
    >> Go to http://localhost:8000
    >> Prosper...

The above creates your basic Django project and provisions your virtual environment so you can start development.  Once
you shell into your vagrant environment the motd will provide you instructions on how to activate your virtualenv
and run your server.

Options
=======
Currently djvasa provides two database options, mysql or postgres, as well as an option to setup your project for deployment
to Heroku.  By default the project is initialized for git usage and creates a .gitignore file, but if you wish to use
mercurial there is a flag for enabling mercurial

::

    >> djvasa -h
    usage: djvasa [-h] [--heroku] [--mysql] [--postgres] [--hg]

    optional arguments:
    -h, --help  show this help message and exit
    --heroku    Initialize the project for deployment to Heroku.
    --mysql     Initialize the project with MySQL.
    --postgres  Initialize the project with Postgres.
    --hg        Initialize project for mercurial.

::

    >> djvasa --mysql


Heroku
------
Djvasa provides an option to set your project up for deployment to Heroku.  Since Heroku uses Postgres as the database,
postgres will automatically be enabled for your project.  Your settings file will contain the necessary Heroku
requirements.  Below is an example:

::

    >> djvasa --heroku
    What's the name of your project? foobar
    What's your full name? Chad Gallemore
    What's your email? cgallemore@gmail.com

    >> cd foobar
    >> git init
    >> git add .
    >> git ci -m"my django app"
    >> heroku create
    >> git push heroku master
    >> heroku run python manage.py syncdb
    >> heroku open


djvasa
======

(Dj)ango - (Va)grant - (Sa)ltStack

This is currently under development, the general idea here is to be able to quickly spin up new Django projects
and get to work.  I'll be utilizing Vagrant to create a virtual environment and will be adding pieces to
also setup other tools needed, like a database.

Currently you can initialize a Django project with the choice of either MySQL or Postgres.  For example, to initialize
with MySQL issue the following command:

    >> djvasa --mysql

This will create the necessary salt states for MySQL and when you run vagrant up MySQL will be installed, started, a user
called django will be created and finally a database named the same as your project will be created.

To initialize Django with Postgres, is the same as MySQL but with the --postgres flag:

    >> djvasa --postgres

Optionally, you can enable Heroku as well with the --heroku flag:

    >> djvasa --heroku

Since Heroku uses Postgres as the database, postgres will automatically be enabled for your project.  Your settings
file will contain the necessary Heroku requirements.  I haven't fully got around to testing this yet, but am getting there.

If you would like to try it, you can do the following, assuming you have Vagrant and Virtualbox installed:

    >> pip install git+git://github.com/cgallemore/djvasa.git
    >> djvasa --mysql
    What's the name of your project? foobar
    What's your full name? Chad Gallemore
    What's your email? cgallemore@gmail.com
    >> cd foobar/
    >> vagrant plugin install vagrant-salt
    >> vagrant up
    >> vagrant ssh
    >> . .virtualenvs/{{project_name}}/bin/activate && cd /vagrant
    >> python manage.py syncdb
    >> python manage.py runserver 0.0.0.0:8000
    >> Go to http://localhost:8000/admin
    >> Prosper...

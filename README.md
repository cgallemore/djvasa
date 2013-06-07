djvasa
======

(Dj)ango - (Va)grant - (Sa)ltStack

This is currently under development, the general idea here is to be able to quickly spin up new Django projects
and get to work.  I'll be utilizing Vagrant to create a virtual environment and will be adding pieces to
also setup other tools needed, like a database.

In it's current state, djvasa will create a functional django project and the necessary Vagrant and SaltStack files to
spin up the environment.  Up next on the list of todo's is adding support for initializing a database in Vagrant.

If you would like to try it, you can do the following, assuming you have Vagrant and Virtualbox installed:

    >> pip install git+git://github.com/cgallemore/djvasa.git
    >> djvasa
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

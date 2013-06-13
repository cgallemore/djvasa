import argparse
import pystache
import os
import random
import sys
from djvasa.templates import *
from djvasa.templates.salt import *


class Project(object):
    def __init__(self, heroku=False, mysql=False, postgres=False):
        self.project_name = raw_input("What's the name of your project? ")
        self.heroku = heroku
        self.mysql = mysql
        self.postgres = postgres
        self.renderer = pystache.Renderer()
        self.project_path = self.project_root = os.path.join(os.getcwd(), self.project_name)

    def _create_file(self, name, template):
        with open(os.path.join(self.project_path, name), 'w+') as f:
            f.write(self.renderer.render(template))

    @property
    def _project_key(self):
        chars = "!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(chars) for c in xrange(50))

    @property
    def _kwargs(self):
        return {
            'heroku': self.heroku,
            'mysql': self.mysql,
            'postgres': self.postgres
        }

    def initialize(self):
        # Create root directory
        os.mkdir(self.project_name)

        # Create manage.py
        self._create_file('manage.py', Manage(self.project_name, **self._kwargs))

        # TODO Create git or hg ignore file

        if self.heroku:
            # Since this is a heroku deployment, we want to enable postgres automatically
            self.postgres = True
            self._create_file('Procfile', Procfile(self.project_name, **self._kwargs))

        self._create_file('Vagrantfile', Vagrantfile(self.project_name, **self._kwargs))

        os.chdir(self.project_path)
        self.project_path = os.path.join(os.getcwd(), self.project_name)
        os.mkdir(self.project_name)
        open(os.path.join(self.project_path, '__init__.py'), 'w+').close()

        # Create settings.py
        kwargs = self._kwargs
        kwargs['secret_key'] = self._project_key
        self._create_file('settings.py', Settings(self.project_name, **kwargs))

        # Create settingslocal.py
        self._create_file('settingslocal.py', SettingsLocal(self.project_name, **self._kwargs))

        # Create urls.py
        self._create_file('urls.py', Urls(self.project_name, **self._kwargs))

        # Create wsgi.py
        self._create_file('wsgi.py', Wsgi(self.project_name, **self._kwargs))

        os.chdir(self.project_root)
        self.project_path = os.path.join(os.getcwd(), 'salt')
        os.makedirs('salt/roots/salt')

        if self.postgres:
            # Create the pillar directories
            os.mkdir('pillar')

        # Create minion
        self._create_file('minion', Minion(self.project_name))

        # Create top.sls
        self.project_path = os.path.join(os.getcwd(), 'salt', 'roots', 'salt')
        self._create_file('top.sls', Top(self.project_name, **self._kwargs))

        # Create project_name.sls
        self._create_file('%s.sls' % self.project_name, SaltProject(self.project_name, **self._kwargs))

        # Create requirements.sls
        self._create_file('requirements.sls', Requirements(self.project_name, **self._kwargs))

        # Create requirements.pip
        self._create_file('requirements.pip', PipRequirements(self.project_name, **self._kwargs))

        if self.mysql:
            self._create_file('mysql.sls', Mysql(self.project_name, **self._kwargs))

        if self.postgres:
            self._create_file('pg_hba.conf', Pgconf(self.project_name, **self._kwargs))
            self._create_file('postgres.sls', Postgres(self.project_name, **self._kwargs))

            # create pillar directory and postgres settings.
            pillar = os.path.join(self.project_root, 'pillar')
            os.chdir(pillar)
            self.project_path = pillar

            self._create_file('top.sls', PillarTop(self.project_name, **self._kwargs))
            self._create_file('settings.sls', PillarSettings(self.project_name, **self._kwargs))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--heroku', action='store_true', default=False, help="Initialize the project for "
                                                                             "deployment to Heroku.")
    parser.add_argument('--mysql', action='store_true', default=False, help='Initialize the project with MySQL.')
    parser.add_argument('--postgres', action='store_true', default=False, help="Initialize the project with Postgres.")
    args = parser.parse_args()

    if args.mysql and args.postgres:
        sys.exit("You can only enable one database, you enabled both MySQL and Postgres.")

    if args.mysql and args.heroku:
        sys.exit("Enable MySQL is not valid with the heroku option.  By default postgres is enabled with "
                 "the heroku option is used.")

    project = Project(heroku=args.heroku, mysql=args.mysql, postgres=args.postgres)
    project.initialize()

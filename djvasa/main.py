import argparse
import pystache
import os
import random
import sys
from djvasa.templates import View


class Project(object):
    def __init__(self, heroku=False, mysql=False, postgres=False):
        self.project_name = raw_input("What's the name of your project? ")
        self.heroku = heroku
        self.mysql = mysql
        self.postgres = postgres or heroku
        self.secret_key = self._project_key
        self.full_name = raw_input("What's your full name? ")
        self.email = raw_input("What's your email? ")
        self.project_path = self.project_root = os.path.join(os.getcwd(), self.project_name)
        self.renderer = pystache.Renderer()
        self.view = View(self.project_name, **self._kwargs)

    def _create_file(self, names):
        for file_name, template_name in names:
            self.view.template_name = template_name
            with open(os.path.join(self.project_path, file_name), 'w+') as f:
                f.write(self.renderer.render(self.view))

    @property
    def _project_key(self):
        chars = "!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(chars) for c in xrange(50))

    @property
    def _kwargs(self):
        return {
            'heroku': self.heroku,
            'mysql': self.mysql,
            'postgres': self.postgres,
            'secret_key': self.secret_key,
            'full_name': self.full_name,
            'email': self.email
        }

    def initialize(self):
        # Create root directory
        os.mkdir(self.project_name)
        root_files = [
            ('manage.py', 'manage'),
            ('requirements.txt', 'pip_requirements'),
            ('Vagrantfile', 'vagrantfile'),
        ]

        # TODO Create git or hg ignore file

        if self.heroku:
            root_files.append(('Procfile', 'procfile'))

        self._create_file(root_files)

        os.chdir(self.project_path)
        self.project_path = os.path.join(os.getcwd(), self.project_name)
        os.mkdir(self.project_name)
        open(os.path.join(self.project_path, '__init__.py'), 'w+').close()

        # Django files
        self._create_file([
            ('settings.py', 'settings'),
            ('settingslocal.py', 'settings_local'),
            ('urls.py', 'urls'),
            ('wsgi.py', 'wsgi')
        ])

        os.chdir(self.project_root)
        self.project_path = os.path.join(os.getcwd(), 'salt')
        os.makedirs('salt/roots/salt')

        if self.postgres:
            # Create the pillar directories
            os.mkdir('pillar')

        # Create minion
        self._create_file([('minion', 'minion')])

        self.project_path = os.path.join(os.getcwd(), 'salt', 'roots', 'salt')
        salt_files = [
            ('top.sls', 'top'),
            ('%s.sls' % self.project_name, 'salt_project'),
            ('requirements.sls', 'requirements')
        ]

        if self.mysql:
            salt_files.append(('mysql.sls', 'mysql'))

        if self.postgres:
            salt_files.append(('pg_hba.conf', 'pgconf'))
            salt_files.append(('postgres.sls', 'postgres'))

        self._create_file(salt_files)

        if self.postgres:
            # create pillar directory and postgres settings.
            pillar = os.path.join(self.project_root, 'pillar')
            os.chdir(pillar)
            self.project_path = pillar

            self._create_file([
                ('top.sls', 'pillar_top'),
                ('settings.sls', 'pillar_settings')
            ])


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

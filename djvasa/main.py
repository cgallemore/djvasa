import argparse
import pystache
import os
import random
from djvasa.templates import *
from djvasa.templates.salt import *


class Project(object):
    project_name = None
    heroku = None

    def __init__(self, heroku=False):
        self.project_name = raw_input("What's the name of your project? ")
        self.heroku = heroku
        self.renderer = pystache.Renderer()
        self.project_path = self.project_root = os.path.join(os.getcwd(), self.project_name)

    def _create_file(self, name, template):
        with open(os.path.join(self.project_path, name), 'w+') as f:
            f.write(self.renderer.render(template))

    @property
    def _project_key(self):
        chars = "!@#$%^&*(-_=+)abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(chars) for c in xrange(50))

    def initialize(self):
        # Create root directory
        os.mkdir(self.project_name)

        # Create manage.py
        self._create_file('manage.py', Manage(self.project_name))

        # TODO Create git or hg ignore file

        # TODO Create Procfile if heroku
        if self.heroku:
            self._create_file('Procfile', Procfile(self.project_name))

        # TODO Make Vagrant optional
        # Create vagrant file if vagrant
        self._create_file('Vagrantfile', Vagrantfile(self.project_name))

        os.chdir(self.project_path)
        self.project_path = os.path.join(os.getcwd(), self.project_name)
        os.mkdir(self.project_name)
        open(os.path.join(self.project_path, '__init__.py'), 'w+').close()

        # Create settings.py
        self._create_file('settings.py', Settings(self.project_name, heroku=self.heroku, secret_key=self._project_key))

        # Create settingslocal.py
        self._create_file('settingslocal.py', SettingsLocal(self.project_name))

        # Create urls.py
        self._create_file('urls.py', Urls(self.project_name))

        # Create wsgi.py
        self._create_file('wsgi.py', Wsgi(self.project_name))

        os.chdir(self.project_root)
        self.project_path = os.path.join(os.getcwd(), 'salt')
        os.makedirs('salt/roots/salt')

        # Create minion
        self._create_file('minion', Minion(self.project_name))

        # Create top.sls
        self.project_path = os.path.join(os.getcwd(), 'salt', 'roots', 'salt')
        self._create_file('top.sls', Top(self.project_name))

        # Create project_name.sls
        self._create_file('%s.sls' % self.project_name, SaltProject(self.project_name))

        # Create requirements.sls
        self._create_file('requirements.sls', Requirements(self.project_name))

        # Create requirements.pip
        self._create_file('requirements.pip', PipRequirements(self.project_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--heroku', action='store_true', default=False,
                        help="Initialize the project for deployment to Heroku.")
    args = parser.parse_args()

    project = Project(heroku=args.heroku)
    project.initialize()

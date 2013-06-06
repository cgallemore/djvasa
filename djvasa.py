import argparse
import pystache
import os
from templates import *


class Project(object):
    project_name = None
    heroku = None

    def __init__(self, project_name, heroku=False):
        self.project_name = project_name
        self.heroku = heroku
        self.renderer = pystache.Renderer()
        self.project_path = os.path.join(os.getcwd(), project_name)

    def _create_file(self, name, template):
        with open(os.path.join(self.project_path, name), 'w+') as f:
            f.write(self.renderer.render(template))

    def initialize(self):
        # Create root directory
        os.mkdir(self.project_name)

        # Create manage.py
        self._create_file('manage.py', Manage(self.project_name))

        # Create requirements file

        # Create git or hg ignore file

        # Create Procfile if heroku

        # Create vagrant file if vagrant

        os.chdir(self.project_path)
        self.project_path = os.path.join(os.getcwd(), self.project_name)
        os.mkdir(self.project_name)

        # Create settings.py
        self._create_file('settings.py', Settings(self.project_name))

        # Create urls.py
        self._create_file('urls.py', Urls(self.project_name))

        # Create wsgi.py
        self._create_file('wsgi.py', Wsgi(self.project_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project', help="The Django project name.")
    args = parser.parse_args()

    project = Project(args.project)
    project.initialize()

import os
import shutil
import tempfile
import unittest
from djvasa import main


class InitializeProjectTestCase(unittest.TestCase):
    def setUp(self):
        super(InitializeProjectTestCase, self).setUp()
        self.root = tempfile.gettempdir()
        os.chdir(self.root)
        self.project_name = 'foobar'
        main.raw_input = lambda x: self.project_name

    def tearDown(self):
        super(InitializeProjectTestCase, self).tearDown()
        shutil.rmtree(os.path.join(self.root, self.project_name))

    def _exists(self, files):
        for f in files:
            self.assertTrue(os.path.exists(f))

    def _validate_salt(self, **kwargs):
        os.chdir(os.path.join(self.root, self.project_name, 'salt'))
        self._exists([
            'minion', 'roots/salt/motd', 'roots/salt/%s.sls' % self.project_name,
            'roots/salt/requirements.sls', 'roots/salt/top.sls'
        ])

    def _validate_project_root(self, **kwargs):
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), self.project_name)))
        self._exists([
            'Vagrantfile', 'manage.py', 'requirements.txt',
        ])
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'salt')))

    def _validate_django(self, **kwargs):
        os.chdir(os.path.join(os.getcwd(), self.project_name))
        self._exists([
            '__init__.py', 'settings.py', 'settingslocal.py', 'urls.py', 'wsgi.py',
            'static/css', 'static/js', 'static/less', 'static/img', 'templates/base.html', 'public'
        ])

    def _kwargs(self, mysql=False, postgres=False, heroku=False, hg=False):
        return {
            'mysql': mysql,
            'postgres': postgres,
            'heroku': heroku,
            'hg': hg
        }

    def test_basic_init(self):
        kwargs = self._kwargs()
        project = main.Project(**kwargs)
        project.initialize()

        self._validate_project_root(**kwargs)
        self._validate_django(**kwargs)
        self._validate_salt(**kwargs)

    # def test_init_with_mysql(self):
    #     pass
    #
    # def test_init_with_postgres(self):
    #     pass
    #
    # def test_init_with_heroku(self):
    #     pass
    #
    # def test_init_with_hg(self):
    #     pass




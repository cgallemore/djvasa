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
        os.chdir(self.root)

    def _exists(self, files):
        for f in files:
            self.assertTrue(os.path.exists(f))

    def _validate_salt(self, **kwargs):
        os.chdir(os.path.join(self.root, self.project_name))
        exists = [
            'salt/minion',
            'salt/roots/salt/motd',
            'salt/roots/salt/%s.sls' % self.project_name,
            'salt/roots/salt/requirements.sls',
            'salt/roots/salt/top.sls'
        ]

        if kwargs['mysql']:
            exists.append('salt/roots/salt/mysql.sls')

        if kwargs['postgres']:
            exists += [
                'salt/roots/salt/postgres.sls',
                'salt/roots/salt/pg_hba.conf',
                'pillar/top.sls',
                'pillar/settings.sls'
            ]

        self._exists(exists)

    def _validate_project_root(self, **kwargs):
        os.chdir(os.path.join(self.root, self.project_name))
        exists = [
            'Vagrantfile',
            'manage.py',
            'requirements.txt',
        ]

        if kwargs['hg']:
            exists.append('.hgignore')
        else:
            exists.append('.gitignore')

        if kwargs['heroku']:
            exists.append('Procfile')

        self._exists(exists)

    def _validate_django(self, **kwargs):
        os.chdir(os.path.join(self.root, self.project_name, self.project_name))
        self._exists([
            '__init__.py',
            'settings.py',
            'settingslocal.py',
            'urls.py',
            'wsgi.py',
            'static/css',
            'static/js',
            'static/less',
            'static/img',
            'templates/base.html',
            'public'
        ])

    def _kwargs(self, mysql=False, postgres=False, heroku=False, hg=False):
        return {
            'mysql': mysql,
            'postgres': postgres or heroku,
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

    def test_init_with_mysql(self):
        kwargs = self._kwargs(mysql=True)
        project = main.Project(**kwargs)
        project.initialize()

        self._validate_project_root(**kwargs)
        self._validate_django(**kwargs)
        self._validate_salt(**kwargs)

    def test_init_with_postgres(self):
        kwargs = self._kwargs(postgres=True)
        project = main.Project(**kwargs)
        project.initialize()

        self._validate_project_root(**kwargs)
        self._validate_django(**kwargs)
        self._validate_salt(**kwargs)

    def test_init_with_heroku(self):
        kwargs = self._kwargs(heroku=True)
        project = main.Project(**kwargs)
        project.initialize()

        self._validate_project_root(**kwargs)
        self._validate_django(**kwargs)
        self._validate_salt(**kwargs)

    def test_init_with_hg(self):
        kwargs = self._kwargs(hg=True)
        project = main.Project(**kwargs)
        project.initialize()

        self._validate_project_root(**kwargs)
        self._validate_django(**kwargs)
        self._validate_salt(**kwargs)




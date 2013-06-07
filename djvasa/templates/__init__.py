__all__ = ('Manage', 'Settings', 'SettingsLocal', 'Urls', 'Wsgi', 'Vagrantfile',)


class Base(object):
    _project_name = None
    _heroku = None

    def __init__(self, *args, **kwargs):
        self._project_name = args[0]
        self._heroku = kwargs.get('heroku', False)

    def project_name(self):
        return self._project_name

    def heroku(self):
        return self._heroku


class Manage(Base):
    """
    Maps to manage.mustache
    """


class Settings(Base):
    """
    Maps to settings.mustache
    """
    name = None
    email = None
    secret_key = None

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.secret_key = kwargs.get('secret_key')
        self.name = raw_input("What's your full name? ")
        self.email = raw_input("What's your email? ")


class SettingsLocal(Base):
    """
    Maps to settingslocal.mustache
    """


class Urls(Base):
    """
    Maps to urls.mustache
    """


class Wsgi(Base):
    """
    Maps to wsgi.mustache
    """


class Vagrantfile(Base):
    """
    Maps to vagrantfile.mustache
    """
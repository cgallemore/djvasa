__all__ = ('Manage', 'Settings', 'SettingsLocal', 'Urls', 'Wsgi',)


class Base(object):
    project_name = None
    heroku = None

    def __init__(self, project_name, heroku=False):
        self.project_name = project_name
        self.heroku = heroku

    def project_name(self):
        return self.project_name


class Manage(Base):
    """
    Maps to manage.mustache
    """


class Settings(Base):
    """
    Maps to settings.mustache
    """


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
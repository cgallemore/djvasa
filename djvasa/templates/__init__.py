from pystache.template_spec import TemplateSpec


class View(TemplateSpec):
    _project_name = None
    _heroku = None
    _mysql = None
    _postgres = None
    template_name = None

    def __init__(self, project_name, **kwargs):
        self._project_name = project_name
        self._heroku = kwargs.get('heroku', False)
        self._mysql = kwargs.get('mysql', False)
        self._postgres = kwargs.get('postgres', False)

    def project_name(self):
        return self._project_name

    def heroku(self):
        return self._heroku

    def mysql(self):
        return self._mysql

    def postgres(self):
        return self._postgres
from pystache.template_spec import TemplateSpec


class View(TemplateSpec):
    template_name = None

    def __init__(self, project_name, **kwargs):
        self.project_name = project_name

        for k, v in kwargs.items():
            setattr(self, k, v)
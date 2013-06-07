from djvasa.templates import Base


__all__ = ('Minion', 'SaltProject', 'Requirements', 'Top', 'PipRequirements')


class Minion(Base):
    """
    Maps to minion.mustache
    """


class SaltProject(Base):
    """
    Maps to salt_project.mustache
    """


class Requirements(Base):
    """
    Maps to requirements.mustache
    """


class Top(Base):
    """
    Maps to top.mustache
    """


class PipRequirements(Base):
    """
    Maps to pip_requirements.mustache
    """
from djvasa.templates import Base


__all__ = ('Minion', 'SaltProject', 'Requirements', 'Top', 'PipRequirements', 'Mysql', 'Postgres', 'Pgconf')


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


class Mysql(Base):
    """
    Maps to mysql.mustache
    """

class Postgres(Base):
    """
    Maps to postgres.mustache
    """


class Pgconf(Base):
    """
    Maps to pgconf.mustache
    """
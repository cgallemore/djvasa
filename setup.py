#!/usr/bin/env python

import os
import sys
from setuptools import setup


def publish():
    os.system('python setup.py sdist upload')

if sys.argv[-1] == 'publish':
    publish()
    sys.exit()

setup(
    name='djvasa',
    version='0.1.0',
    description='Initialize a new Django project with Vagrant for easy start',
    long_description='',
    author='Chad Gallemore',
    author_email='cgallemore@gmail.com',
    url='https://github.com/cgallemore/djvasa',
    license='BSD',
    packages=['djvasa', 'djvasa.templates'],
    package_data={'djvasa': ['templates/*.mustache']},
    entry_points={
        'console_scripts': ['djvasa = djvasa.main:main'],
    },
    install_requires=[
        "pystache >= 0.5.3",
    ],
)

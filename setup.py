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
    url='',
    license='BSD',
    entry_points={
        'console_scripts': ['djvasa = djvasa:main'],
    },
    install_requires=[
        "pystache >= 0.5.3",
    ],
)

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
    long_description=open('README.rst').read(),
    author='Chad Gallemore',
    author_email='cgallemore@gmail.com',
    url='https://github.com/cgallemore/djvasa',
    license='MIT',
    keywords='terminal django vagrant saltstack cli',
    classifiers=(
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ),
    packages=['djvasa', 'djvasa.templates'],
    package_data={'djvasa': ['templates/*.mustache']},
    entry_points={
        'console_scripts': ['djvasa = djvasa.main:main'],
    },
    install_requires=[
        "pystache >= 0.5.3",
    ],
)

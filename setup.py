#!/usr/bin/env python

import os
import sys
from setuptools import setup


def publish():
    os.system('python setup.py sdist upload')

if sys.argv[-1] == 'publish':
    publish()
    sys.exit()

current_version = sys.version_info[:2]
optional_requirements = []
if current_version < (2, 7) or current_version == (3, 1) or (3, 2):
    optional_requirements.append('argparse>=1.2.1')

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
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ),
    packages=['djvasa', 'djvasa.templates'],
    package_data={'djvasa': ['templates/*.mustache']},
    entry_points={
        'console_scripts': ['djvasa = djvasa.main:main'],
    },
    install_requires=[
        "pystache >= 0.5.3",
    ] + optional_requirements,
)

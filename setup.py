# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cookie
version = cookie.__version__

setup(
    name='cookiecutter',
    version=version,
    author='',
    author_email='fabio.ar.rodrigues@gmailcom',
    packages=[
        'cookie',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['cookie/manage.py'],
)
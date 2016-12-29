#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-template-minifier',
    version='1.1.0',
    description='Python package, providing simple django template loader. It reduces HTML output in templates '
                'by stripping out whitespace characters between HTML and django template tags.',
    author='Leszek Piatek',
    author_email='lpiatek@gmail.com',
    url='https://github.com/iRynek/django-template-minifier',
    license='GPL',
    packages=[
        'template_minifier',
        'template_minifier.template',
        'template_minifier.template.loaders',
    ],
    requires=[
        'Django(>=1.9)',
    ],
)

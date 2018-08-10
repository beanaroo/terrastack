# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='terrastack',
    version='0.1.0',
    description='Create terraform specifications with code',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Frank Hammar',
    author_email='frank@frankotron.se',
    url='https://github.com/frankotron/terrastack',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
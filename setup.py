# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='terrastack',
    version='0.1.0',
    description='Create terraform specifications with code',
    long_description=readme,
    author='Frank Hammar',
    author_email='frank@frankotron.se',
    url='https://github.com/frankotron/terrastack',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
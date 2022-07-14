# -*- coding: utf-8 -*-
import setuptools

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='sample',
    version='0.0.1',
    description='package for okta-Oauth',
    long_description=readme,
    author='yentl creyf',
    author_email='',
    url='https://github.com/yentl-creyf/okta-Oauth',
    license=license,
    packages=setuptools.find_packages(exclude=('tests', 'docs'))
)

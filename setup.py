# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in logistic_management/__init__.py
from logistic_management import __version__ as version

setup(
	name='logistic_management',
	version=version,
	description='Logistic Management',
	author='Raj Tailot',
	author_email='tailorraj111@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

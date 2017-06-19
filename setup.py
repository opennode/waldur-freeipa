#!/usr/bin/env python
from setuptools import setup, find_packages


install_requires = [
    'nodeconductor>0.141.0',
    'python_freeipa>=0.1.2',
]


tests_requires = [
    'ddt>=1.0.0,<1.1.0',
    'factory_boy==2.4.1',
    'freezegun==0.3.7',
    'mock>=1.0.1',
    'mock-django==0.6.9',
    'six>=1.9.0',
    'sqlalchemy>=1.0.12',
]


setup(
    name='waldur-freeipa',
    version='0.2.0',
    author='OpenNode Team',
    author_email='info@opennodecloud.com',
    url='http://waldur.com',
    description='FreeIPA plugin for Waldur MasterMind',
    long_description=open('README.rst').read(),
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=install_requires,
    extras_require={
        'tests': tests_requires,
    },
    zip_safe=False,
    entry_points={
        'nodeconductor_extensions': (
            'waldur_freeipa = waldur_freeipa.extension:FreeIPAExtension',
        ),
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)

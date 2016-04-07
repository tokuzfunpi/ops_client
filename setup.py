#!/usr/bin/python
from setuptools import setup, find_packages

name = 'ops_client'

setup(
    name=name,
    version='0.0.1',
    description='Openstack Client',
    license='Apache License (2.0)',
    author='Joe Yang',
    author_email='tokuzfunpu@gmail.com',
    url='',
    packages=find_packages(exclude=['test', 'bin']),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[],
    scripts=[],
    entry_points={})

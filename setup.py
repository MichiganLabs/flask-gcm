#!/usr/bin/env python

"""
Setup script for Flask-GCM.
"""

import setuptools

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name='Flask-GCM',
    version='0.2.1',

    description="Flask-GCM is a simple wrapper for the python-gcm library to be used with Flask applications.",
    url='https://github.com/michiganlabs/flask-gcm',
    author='Josh Friend',
    author_email='jfriend@michiganlabs.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=open('requirements.txt').readlines(),
)

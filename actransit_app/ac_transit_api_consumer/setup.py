#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ac_transit_api_consumer',
    version='0.0.1',
    description="Python consumer/client library for consuming AC Transit's REST APIs.",
    long_description=readme + '\n\n' + history,
    author="Sidharth Mishra",
    author_email='sidharth.mishra@sjsu.edu',
    url='https://github.com/sidmishraw/ac_transit_api_consumer',
    packages=[
        'ac_transit_api_consumer',
    ],
    package_dir={'ac_transit_api_consumer':
                 'ac_transit_api_consumer'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='ac_transit_api_consumer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

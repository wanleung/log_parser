#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Wan Leung Wong",
    author_email='wanleung@wanleung.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python log parser to parse weblog to get views count of paths",
    entry_points={
        'console_scripts': [
            'log_parser=log_parser.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='log_parser',
    name='log_parser',
    packages=find_packages(include=['log_parser', 'log_parser.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wanleung/log_parser',
    version='0.1.0',
    zip_safe=False,
)

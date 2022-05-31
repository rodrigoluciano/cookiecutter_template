#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Rodrigo Luciano da Costa",
    author_email='rodrigolucianocosta@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="test de aplicação com template",
    entry_points={
        'console_scripts': [
            'python_data_science=python_data_science.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python_data_science',
    name='python_data_science',
    packages=find_packages(include=['python_data_science', 'python_data_science.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rodrigoluciano/python_data_science',
    version='0.0.1',
    zip_safe=False,
)

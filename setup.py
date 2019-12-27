# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='hello_world',
    version='0.1.0',
    description='Sample package for Hello world',
    long_description=readme,
    author='BRISKbaby  ',
    author_email='31022759+BRISKbaby@users.noreply.github.com',
    url='https://github.com/BRISKbaby/hello_world',
    license="tbd",
    packages=find_packages(exclude=('tests', 'docs')),
    tests_require=["pytest", "pytest-cov"],
    setup_requires=(
        'pytest-runner',
    ),
)

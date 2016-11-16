#!/usr/bin/env python

from distutils.core import setup, find_packages

setup(
    name='jgutils',
    version='1.0',
    description='Useful functions for doing handy stuff.',
    author='James Gilbert',
    url='https://www.labjg.com',
    packages=find_packages(),
    install_requires=['numpy'],
    )

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A filter for Pygments that extracts a code snippet based on a range of line numbers.
"""
from setuptools import setup

setup(
    name='SnippetFilter',
    version='0.1.dev',
    author='Julius Adorf',
    author_email='jeadorf@gmx.de',
    description=__doc__,
    long_description=__doc__,
    packages = [''],
    platforms = 'any',
    license='BSD License',
    keywords='pygments plugin filter line snippet',
    url='http://bitbucket.org/jeadorf/pygments-snippet-filter',
    test_suite='test_snippetfilter',
    entry_points='''
    [pygments.filters]
    snippet = snippetfilter:SnippetFilter
    '''
)


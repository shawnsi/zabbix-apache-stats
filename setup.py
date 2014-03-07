#!/usr/bin/env python

from setuptools import setup

setup(
    name='zabbix-apache-stats',
    version='0.0.1',
    author='Paulson McIntyre',
    author_email='paul@gpmidi.net',
    description='Zabbix Apache Stat Collector',
    license = 'GPLv2',
    package_dir = {'': 'bin'},
    py_modules = ['fetch'],
)


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
CloudBridge provides a uniform interface to multiple IaaS cloud providers.
"""

import ast
import os
import re

from setuptools import find_packages
from setuptools import setup

# Cannot use "from cloudbridge import get_version" because that would try to
# import the six package which may not be installed yet.
reg = re.compile(r'__version__\s*=\s*(.+)')
with open(os.path.join('cloudbridge', '__init__.py')) as f:
    for line in f:
        m = reg.match(line)
        if m:
            version = ast.literal_eval(m.group(1))
            break

REQS_BASE = [
    'six>=1.11',
    'tenacity>=6.0',
    'deprecation>=2.0.7',
    'pyeventsystem<2'
]
REQS_AWS = [
    'boto3>=1.9.86,<1.17'
]
# Install azure>=3.0.0 package to find which of the azure libraries listed
# below are compatible with each other. List individual libraries instead
# of using the azure umbrella package to speed up installation.
REQS_AZURE = [
    'msrest>=0.5.4,<0.6',
    'msrestazure==0.5.0',
    'azure-common==1.1.14',
    'azure-mgmt-devtestlabs==2.2.0',
    'azure-mgmt-resource==2.0.0',
    'azure-mgmt-compute==4.0.1',
    'azure-mgmt-network>=2.0.1,<=2.1',
    'azure-mgmt-storage==2.0.0',
    'azure-storage-blob==1.3.1',
    'azure-cosmosdb-table==1.0.4',
    'pysftp==0.2.9'
]
REQS_GCP = [
    'google-api-python-client>=1.7.8,<1.13',
    'oauth2client<4.2'
]
REQS_OPENSTACK = [
    'openstacksdk>=0.12.0,<0.53',
    'python-novaclient>=7.0.0,<17.3',
    'python-swiftclient>=3.2.0,<3.11',
    'python-neutronclient>=6.0.0,<7.3',
    'python-keystoneclient>=3.13.0,<4.2'
]
REQS_SIMPLE = REQS_BASE + REQS_AWS + REQS_GCP + REQS_OPENSTACK
REQS_AZURE = REQS_SIMPLE + REQS_AZURE
REQS_FULL = REQS_SIMPLE + REQS_AZURE
# httpretty is required with/for moto 1.0.0 or AWS tests fail
REQS_DEV = ([
    'tox>=2.1.1',
    'nose',
    'moto>=1.3.2',
    'sphinx>=1.3.1',
    'pydevd',
    'flake8>=3.3.0',
    'flake8-import-order>=0.12'] + REQS_FULL
)

setup(
    name='cloudbridge',
    version=version,
    description='A simple layer of abstraction over multiple cloud providers.',
    long_description=__doc__,
    author='Galaxy and GVL Projects',
    author_email='help@genome.edu.au',
    url='http://cloudbridge.cloudve.org/',
    setup_requires=['nose>=1.0'],
    install_requires=REQS_SIMPLE,
    extras_require={
        ':python_version<"3.3"': ['ipaddress'],
        'azure': REQS_AZURE,
        'full': REQS_FULL,
        'dev': REQS_DEV
    },
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'],
    test_suite="tests"
)

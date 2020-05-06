# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='importsize',
    version='2020.1.1',
    description='Use this module to get the sizes of used imports in a project',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/ImportSize/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/ImportSize",
        "repository":
            "https://github.com/FHPythonUtils/ImportSize"
    },
    author='FredHappyface',
    classifiers=[
        'Environment :: Console', 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={"console_scripts": ["importsize = importsize:cli"]},
    packages=['ImportSize'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'pip==20.*,>=20.0.2', 'pipreqs==0.*,>=0.4.10', 'requests==2.*,>=2.23.0'
    ],
)

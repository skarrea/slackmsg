#!/usr/bin/env python

import glob
import os
import sys
from shutil import rmtree
from setuptools import Command, find_packages, setup
from setuptools.command.test import test as TestCommand


def read(fname):
    """
    Read the contents of a file.

    Parameters
    ----------
    fname : str
        Path to file.

    Returns
    -------
    str
        File contents.
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


install_requires = read("requirements.txt").splitlines()

# Import meta data from __meta__.py
#
# We use exec for this because __meta__.py runs its __init__.py first,
# __init__.py may assume the requirements are already present, but this code
# is being run during the `python setup.py install` step, before requirements
# are installed.
# https://packaging.python.org/guides/single-sourcing-package-version/
meta = {}
exec(read("slackmsg/__meta__.py"), meta)

# Import the README and use it as the long-description.
# If your readme path is different, add it here.

# Handle turning a README file into long_description
readme_fname = "README.md"
long_description = read(readme_fname)

long_description_content_type = "text/markdown"

setup(
    # Essential details on the package and its dependencies
    name=meta["name"],
    version=meta["version"],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_dir={meta["name"]: os.path.join(".", meta["path"])},
    # If any package contains *.txt or *.rst files, include them:
    package_data={"": ["*.json"],},
    python_requires=">=3.6",
    install_requires=install_requires,
    # Metadata to display on PyPI
    author=meta["author"],
    author_email=meta["author_email"],
    description=meta["description"],
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    license=meta["license"],
    url=meta["url"],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points = {'console_scripts': [
            'slackmsg = slackmsg.msg:main',
        ]}
)

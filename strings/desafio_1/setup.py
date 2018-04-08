# -*- coding: utf-8 -*-

"""Setup.

API setup file.

"""

import os
from setuptools import setup


def read_file(file_name):
    """Read the file.

    Reads the contents of the file.

    Args:
        file_name (string): Name of the file.

    Returns:
        string: Content of the file.

    """
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="strings_formatter",
    version="0.0.1",
    author="Gustavo Correia Gonzalez",
    author_email="gustavogonzalez@alunos.utfpr.edu.br",
    description=("Api to format strings"),
    keywords="String Limit Caracter",
    packages=['strings_formatter'],
    long_description=read_file('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Hug"
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3.6",
    ]
)

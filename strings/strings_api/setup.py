import os
from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_reqs = parse_requirements("./requirements.txt", session=PipSession())

requires = [str(ir.req) for ir in install_reqs]

setup(
    name="strings_api",
    version="0.0.1",
    author="Gustavo Correia Gonzalez",
    author_email="gustavogonzalez@alunos.utfpr.edu.br",
    description=("Api to format strings"),
    keywords="String Limit Caracter",
    packages=['strings_api'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Hug"
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=requires
)

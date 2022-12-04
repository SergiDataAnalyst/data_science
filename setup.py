from distutils.core import setup
from setuptools import find_packages

setup (
    name="snowflake",
    version="0.1",
    author="Sergi",
    author_email="sergi.molina@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
    )

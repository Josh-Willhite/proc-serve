import os
from setuptools import setup

setup(
    name = "proc-server",
    version = "0.0.1",
    author = "Josh Willhite",
    author_email = "jwillhite@gmail.com",
    description = ("Serve a subset of proc files as json."),
    install_requires=['flask'],
    packages=['src'],
)

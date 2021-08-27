#!/usr/bin/env python
from setuptools import setup
from __version__ import v3rsion

required = [
  'base64', 'random'
]

setup(
  name = "encrypt-it",
  version = v3rsion,
  description = "A simple command line program that will create a password for you, and then give you the option to encrypt it with a specific method.",
  author = "Hifumi-Sec",
  url = "https://github.com/Hifumi-Sec/encrypt-it",
  requires = required,
)
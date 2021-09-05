#!/usr/bin/env python
from setuptools import setup
from __version__ import v3rsion

required = [
  'base64', 'random', 'cryptography', 'rsa'
]

setup(
  name = "encrypt-it",
  version = v3rsion,
  description = "Simple password generator offering various encryption methods.",
  author = "Hifumi-Sec",
  url = "https://github.com/Hifumi-Sec/encrypt-it",
  requires = required,
)
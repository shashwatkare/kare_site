#!/usr/bin/env python
# flake8: noqa

from setuptools import find_packages, setup

dependencies = []

setup(name="kare-ui",
      version="1.1.0",
      description="my portfolio website",
      author="Shashwat Kare",
      author_email="skare@my.bridgeport.edu",
      packages=find_packages(),
      install_requires=dependencies,
      include_package_data=True,
      python_requires=">=3.8",
      test_suite="tests")

# Copyright 2015, Truveris Inc.

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from overpunch import __version__


setup(
    name="overpunch",
    version=__version__,
    description="Overpunch Parser/Formatter",
    author="Truveris Inc.",
    author_email="dev@truveris.com",
    url="http://github.com/truveris/overpunch",
    test_suite="nose.collector",
    packages=find_packages(exclude=["ez_setup"]),
)


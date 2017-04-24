# Copyright 2015-2017, Truveris Inc. All Rights Reserved.

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
    classifiers=[
        "Intended Audience :: Healthcare Industry",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing",
    ],
)


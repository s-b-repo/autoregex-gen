# setup.py

from setuptools import setup, find_packages

setup(
    name="auto_regex_gen",
    version="0.1.0",
    description="A Python library to generate regex patterns from plain English descriptions.",
    author="stefan bothes",
    author_email="ixl0cepkn@mozmail.com",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

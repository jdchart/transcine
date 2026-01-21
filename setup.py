from setuptools import setup
from setuptools import find_packages

long_description = """
# transcine
dlvhjcsd
"""

required = []

setup(
    name = "transcine",
    version = "0.0.1",
    description = "A python package for video transcription",
    long_description = long_description,
    author = "Jacob Hart",
    author_email = "jacob.dchart@gmail.com",
    url = "https://github.com/jdchart/transcine",
    install_requires = required,
    packages = find_packages()
)
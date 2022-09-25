"""Python setup.py for test_python_project package"""
import io
import os

from setuptools import find_packages
from setuptools import setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("test_python_project", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


console_script = "test_python_project = test_python_project.__main__:main"

setup(
    name="test_python_project",
    version=read("test_python_project", "VERSION"),
    description="Awesome test_python_project created by blink1073",
    url="https://github.com/blink1073/test-python-project/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="blink1073",
    packages=find_packages(exclude=["tests", ".github"]),
    entry_points={"console_scripts": [console_script]},
)

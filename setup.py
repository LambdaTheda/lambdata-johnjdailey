# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="buyholdsell",  # the name that you will install via pip
    version="1.9.7",
    author="John Dailey",
    author_email="johnjdailey@email.com",
    description="Import Yahoo Finance data from URL, automatically split, feature engineer, drop Date column, and prepare for predictive modeling.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/johnjdailey/lambdata-johnjdailey",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)

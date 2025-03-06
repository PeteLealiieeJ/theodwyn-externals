import os
from setuptools import setup, find_packages

with open( os.path.join("theodwyn_externals","version.txt") ) as file:
    __version__ = file.read().strip()

_long_description = \
"""
This repository provides a simple structure for interfacing and spinning up components of manipulator systems that actuate vision sensors -- processing and transmitting relevant data necessary to system operations. In our experience, setting up hardware communication in manipulated camera systems often involves an identical workflow across various system configurations. This observation has encouraged us to present a python package which allows users to approach interfacing these components in a simple and modular fashion.

## Links

Repository:
https://github.com/PeteLealiieeJ/theodwyn-externals


## Example
config = StackConfiguration()
# ...
# Load configuration parameters
# ...
stack = ExampleStack( config=config )
stack.spin()
"""

setup(
    name="theodwyn_externals",
    packages=[package for package in find_packages() if package.startswith("theodwyn_externals")],
    package_data={"theodwyn_externals": ["py.typed", "version.txt"]},
    install_requires=[
        "numpy", 
        "pygame",
        "adafruit-circuitpython-servokit",
    ],
    extras_require={
        "tests": [
            # For Testing Packages
            "pytest",
        ],
    },
    description="Python Stack for Vision Based Control of Robotic Systems",
    author="Pete Lealiiee Jr.",
    url="https://github.com/PeteLealiieeJ/theodwyn-externals",
    author_email="petelealiieejr4@utexas.edu",
    keywords="embedded-systems visuomotor-control",
    license="GNU",
    long_description=_long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.8",
    project_urls={
        "Code": "https://github.com/PeteLealiieeJ/theodwyn-externals",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
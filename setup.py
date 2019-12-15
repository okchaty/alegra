import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

with open(
    os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

setuptools.setup(
    author="Chaty",
    author_email="developer@okchaty.com",
    name="alegra",
    license="MIT",
    description="alegra is a python package for connect to the Alegra's API.",
    version="0.1.0",
    long_description=long_description,
    url="https://github.com/okchaty/alegra",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.5",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
)

from distutils.core import setup

setup(
    # Application name:
    name="streaker",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Aldi Alimucaj",
    author_email="aldi.alimucaj@gmail.com",

    # Packages
    packages=["streaker"],

    scripts=['bin/streaker'],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/Streaker_v001/",

    #
    license="MIT",
    description="GitHub streak manipulator",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        # "",
    ],
)

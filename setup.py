import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="Learnig-unit-tests",
    version=version,
    author="Shizo15",
    author_email="damianszymczyk153@gmail.com",
    description="Attendance management system for university",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shizo15/Learnig-unit-tests",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    # entry_points={
    #     "console_scripts": ["teilnahme=src.cli.cli:main"],
    # },
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    python_requires=">=3.12",
)
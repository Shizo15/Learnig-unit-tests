import os
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv("VERSION", "0.0.0")

setup(
    name="Learnig-unit-tests",
    version=version,
    author="Shizo15",
    author_email="damianszymczyk153@gmail.com",
    description="Student attendance management application",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Shizo15/Learnig-unit-tests",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.13",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "attendanceTool=src.task1:menu",
        ],
    },
)

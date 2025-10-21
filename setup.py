from setuptools import setup,find_packages
from typing import List

def requirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path,'r') as f:
        package = f.readlines()
        requirements = [req.strip().replace('\n','') for req in package if not req.startswith('-e')]

    return requirements


setup(
    name='titanic project',
    version='0.0.1',
    author='Akash Raj',
    author_email='akash.raj.dhn@gmail.com',
    packages=find_packages(),                           #it will search for __ini__.py from all the folder and create packages
    requires=['requirements.txt']                       #this is required to install to use this package
)
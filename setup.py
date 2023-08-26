from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'ritik',
    author_email = 'ritiksachdeva50@iitkgp.ac.in',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
from setuptools import setup, find_packages
from typing import List

HUPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:

    '''
    This function will read the requirements from the file and return the list of requirements
    '''
    reqruirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HUPEN_E_DOT in requirements:
            requirements.remove(HUPEN_E_DOT)
    return requirements

setup(
    name="mlprojects",
    version="0.0.1",
    author="Sagar",
    author_email="sagarbhagwatkar99@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
        
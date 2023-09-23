from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='san',
    author_email='sanraj1317@gmail.com',
    packages=find_packages(),
    ## install_requires=['numpy','pandas']
    install_requires=get_requirements('requirements.txt')
)
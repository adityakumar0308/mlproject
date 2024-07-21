from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    returns a list of requirements by reading the file
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] 
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
         
         
    

setup(
name='ds-project',
version='1.0.0',
author='Aditya',
author_email='adityabidhuri15@gmail.com',
author_github='adityakumar0308',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

    
)
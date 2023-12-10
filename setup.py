from setuptools import setup,find_packages
from typing import List


def get_requirments(file_path:str)->list[str]:
    requirments=[]

    with open(file_path) as file_obj:
        requirment=file_obj.readlines()
        requirments=[req.strip() for req in requirment]
    return requirments

setup(name="mytrail",
    version="0.1",
    author="chinmaya",
    author_email="chinmayasahoo@gmail.com",
    description="this is my trail app which was build by me",
    packages=find_packages(),
    install_requires= get_requirments('requirement.txt')
    
    )
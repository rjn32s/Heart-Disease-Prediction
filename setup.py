from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list: List[str] = []

    with open('requirements.txt', 'r') as f:
        for line in f:
            # Skip empty lines and comments
            line = line.strip()
            if line and not line.startswith('#'):
                requirement_list.append(line)

    return requirement_list

setup(
    name="Hear Disease Prediction",
    version="0.0.1",
    author="ineuron",
    author_email="rshukla2k@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

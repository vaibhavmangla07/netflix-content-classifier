from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path, encoding="utf-8") as f:
        requirements = [req.strip() for req in f.readlines() if req.strip()]

    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements


setup(
    name="netflix_data_science_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    description="An end-to-end data science project for Netflix content analysis and classification.",
    author="Vaibhav Mangla",
    author_email="vmangla0704@gmail.com",
)

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = '0.0.0'
REPO_NAME = 'Tomato-leaf-diseases'
AUTHOR_USER_NAME = 'lakiet1609'
SRC_REPO = 'TomatoDiseases'
AUTHOR_EMAIL = 'kiettuanminhla1609@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for CNN app',
    long_description=long_description,
    long_description_content = 'text/markdown',
    url='https://github.com/lakiet1609/project3',
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)
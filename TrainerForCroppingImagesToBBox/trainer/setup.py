from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
  'pillow==4.0.0', 'tensorflow==1.0.1'
]

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    requires=[]
)

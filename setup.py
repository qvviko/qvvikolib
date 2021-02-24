
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='qvvikolib',
      version='0.0.2',
      description='Utils by qvviko',
      long_description=long_description,
      author='Vladislav Savchuk',
      author_email='qvviko@gmail.com',
      license='MIT',
      url="https://github.com/qvviko/qvvikolib",
      packages=['qvvikolib'],
      zip_safe=False)
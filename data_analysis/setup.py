import os

from setuptools import setup, find_packages

setup(name='data-analysis',
      version='1.0',
      description='Data analysis application',
      author='Kevin Teague',
      author_email='kevin@bud.ca',
      url='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
)

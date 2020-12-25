"""
A Better HomeBrew Package Search

Usage: brewls [keyword]

"""

from setuptools import setup

setup(name='curlpy',
      version='0.12',
      description='A python wrapper for curlconverter',
      url='http://github.com/kkatayama/curlpy',
      author='Teddy',
      author_email='katayama@udel.edu',
      license='MIT',
      packages=['curlpy'],
      python_requires='>=3',
      scripts=['bin/curlpy'],
      zip_safe=False)

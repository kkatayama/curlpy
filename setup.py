from setuptools import setup

setup(name='curlpy',
      version='0.14',
      description='A python wrapper for curlconverter',
      url='http://github.com/kkatayama/curlpy',
      author='Teddy',
      author_email='katayama@udel.edu',
      license='MIT',
      packages=['curlpy'],
      python_requires='>=3',
      entry_points={
          'console_scripts': ['curl-py=curlpy.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
      name='openmoticssdk',
      version='0.0.1',
      description=("Python SDK for OpenMotics Gateway"),
      long_description=("Python SDK for OpenMotics Gateway"),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP'],
      author='Andrew Svetlov',
      author_email='andrew.svetlov@gmail.com',
      url='https://github.com/woutercoppens/openmoticssdk/',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      #setup_requires=['pytest-runner'],
      #tests_require=['pytest'],
      include_package_data=False)

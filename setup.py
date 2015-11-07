from setuptools import setup, find_packages

setup(name='trip-service',
    version='0.0.4',
    author='scm',
    description ='refactor kata',
    platforms = 'Linux',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    )

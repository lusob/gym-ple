from setuptools import setup, find_packages
import sys, os.path

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym_ple'))

setup(name='gym_ple',
      version=0.1,
      description='This package allows to use PLE as a gym environment.',
      url='https://github.com/lusob/gym-ple',
      author='Lusob',
      author_email='luis@sobrecueva.com',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('gym')],
      zip_safe=False,
)

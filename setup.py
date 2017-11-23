from setuptools import setup

setup(
   name='HeftyNumber',
   version='0.0.1',
   description='HeftyNumber is a library built upon Numpy for doing arithmetic in arbitrary bases with arbitrary precision. ',
   author='Andrew Riberio',
   author_email='andrew@kexp.io',
   packages=['HeftyNumber'],  #same as name
   install_requires=['numpy','math'], #external packages as dependencies
)
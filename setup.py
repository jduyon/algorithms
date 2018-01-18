from setuptools import setup

setup(name='algorithms',
      version='0.1',
      description='Algorithm and fundamental data structure implementations of computer science',
      url='http://github.com/jduyon/algorithms',
      author='Jake Duyon',
      license='MIT',
      packages=['sorts','partitions','inputs','util','structs'],
      install_requires=[
          'nose',
      ],
      zip_safe=False)

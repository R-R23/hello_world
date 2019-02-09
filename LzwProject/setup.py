from setuptools import setup

setup(name='LZW De/Compressor',
      version='0.1',
      description='De/Compressor, single file or recursive using lzw alg. fixed dictionary length',
      author='Degli Esposti Riccardo',
      packages=['lzw'],
      install_requires=[
          'typing'
          'argparse'
          'setuptools'
      ],
      scripts=['scripts/compress','scripts/uncompress'])

from setuptools import setup

setup(name='LZW De/Compressor',
      version='0.1',
      description='De/Compressor, single file or recursive using lzw alg. fixed dictionary length',
      url='...',
      author='Degli Esposti Riccardo',
      author_email='...',
      packages=['funniest'],
      install_requires=[
          'math',
          'os',
          'typing'
      ],
      scripts=['scripts/compress.sh','scripts/uncompress.sh'])

from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


install_requires = [
  'numpy == 1.16.6',  # REQ: vector algebra operations
  'click',            # REQ: command line interfacing
  'pandas',           # REQ: (conda) sparx.data.filter()

]

setup(name='cognito',
      version='0.0.1',
      description=u"Auto ML Dataset Transformer",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Bastin Robins .J",
      author_email='robin@cleverinsight.co',
      url='https://github.com/cleverinsight',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      cognito=cognito.scripts.cli:cli
      """
      )

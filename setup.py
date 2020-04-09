"""
Cognito module
"""
from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


REQUIRES = [
    'tqdm',
    'numpy',  # REQ: vector algebra operations
    'scipy',
    'numpy',
    'click',            # REQ: command line interfacing
    'pandas',           # REQ: (conda) sparx.data.filter()
    'PyYAML',
    'pyfiglet',
    'datefinder',
    'PrettyTable',
    'scikit-learn'
]


CLASSIFIERS = [
    'Development Status :: 0.0.1 - Beta',
    'Environment :: Multiple',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]


setup(name='cognito',
      version='0.0.1',
      description=u"Auto ML Dataset Transformer",
      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      keywords='',
      author=u"Bastin Robins .J",
      author_email='robin@cleverinsight.co',
      url='https://github.com/cleverinsight',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIRES,

      extras_require={
          'test': ['pytest'],
      },

      entry_points="""
      [console_scripts]
      cognito=cognito.scripts.cli:cli
      """)

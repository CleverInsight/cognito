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
    'numpy',            # REQ: vector algebra operations
    'scipy',
    'numpy',
    'click',            # REQ: command line interfacing
    'pandas',           # REQ: (conda) sparx.data.filter()
    'tornado',          # REQ: report generation engine
    'PyYAML',           # REQ: configuration management
    'pyfiglet',         # REQ: better cli interface  
    'datefinder',     
    'PrettyTable',
    'sparklines',
    'scikit-learn'
]


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    "Operating System :: OS Independent",
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
    'Topic :: Scientific/Engineering'

]


DOWNLOAD_URL = ""
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/Cleverinsight/congito/issues",
    "Documentation": "https://cognito.readthedocs.io/en/latest/",
    "Source Code": "https://github.com/Cleverinsight/congito",
}


setup(name='cognito',
      version='0.0.1b2',
      description=u"Auto ML Dataset Transformer & Auto Data Storyteller",
      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      keywords=['Automated Data Storyteller', 'Data Wrangler', 'Data Preprocessing',\
       'Machine Learning', 'Hot Encoder', 'Outlier Detection'],
      author=u"Bastin Robins .J",
      author_email='robin@cleverinsight.co',
      url='https://github.com/cleverinsight',
      download_url='https://github.com/CleverInsight/cognito/releases',
      project_urls=PROJECT_URLS,
      license='BSD',
      packages=[pkg for pkg in find_packages() if not pkg.startswith('test')],
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

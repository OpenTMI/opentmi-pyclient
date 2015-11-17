import os
from distutils.core import setup
from setuptools import find_packages

DESCRIPTION = "tmt-client"
OWNER_NAMES = 'Jussi Vatjus-Anttila'
OWNER_EMAILS = 'jussiva@gmail.com'


# Utility function to cat in a file (used for the README)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='tmt-client',
      version='0.0.1',
      description=DESCRIPTION,
      long_description=read('README.md'),
      author=OWNER_NAMES,
      author_email=OWNER_EMAILS,
      maintainer=OWNER_NAMES,
      maintainer_email=OWNER_EMAILS,
      url='https://bitbucket.org/_tmt_/tmt-client-python.git',
      packages=find_packages(exclude=['test', 'log', 'htmlcov']),
      package_data={'': ['tc_schema.json']},
      include_package_data=True,
      license="MIT",
      tests_require=["coverage"],
      test_suite = 'test',
      entry_points={
          "console_scripts": [
              "tmtclient=tmt_client:tmt_client_main",
          ]
      },
      install_requires=[
          "requests",
          "jsonmerge"
      ]
    )
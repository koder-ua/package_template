from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='package_template',
      version=version,
      description="default template for package",
      long_description="""\
default template for package""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='koder',
      author_email='koder.mail@gmail.com',
      url='https://github.com/koder-ua',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.paster_create_template]
      package_template = package_template:PackageTemplate
      """,
      )

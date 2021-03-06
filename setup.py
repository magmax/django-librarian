# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from librarian import APP


def read_description():
    with open('README.rst') as fd:
        return fd.read()


setup(name='django-librarian',
      version=APP.version,
      description=APP.description,
      long_description=read_description(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      keywords='book,books,library,librarian,loan,rent',
      author='Miguel Ángel García',
      author_email='miguelangel.garcia@gmail.com',
      url='https://github.com/magmax/django-librarian',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django >= 1.6',
          'django-files >= 1.1',
          # Non free for commercial software
          'django-suit == 0.2.12',
      ],
      )

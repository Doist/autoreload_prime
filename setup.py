#!/usr/bin/env python
import os
from setuptools import setup

setup(name='autoreload_prime',
      version = '1.0',
      author="amix the lucky stiff",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['autoreload_prime'],
      platforms=["Any"],
      license="BSD",
      keywords='autoreload auto reload',
      description="An auto reload module that should work with most servers (patched from Tornado)",
      long_description="""\
autoreload_prime
---------------

An auto reload module that should work with most servers (patched from Tornado).

To install autoreload_prime simply do::

    $ sudo easy_install autoreload_prime

TO use autoreload_prime::

    import autoreload_prime
    autoreload_prime.start()
""")

#-*- coding: UTF-8 -*-

# The three lines below are required to run on EL6 as EL6 has
# two possible version of python-sqlalchemy and python-jinja2
# These lines make sure the application uses the correct version.
import __main__
__main__.__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

import os
## Set the environment variable pointing to the configuration file
os.environ['PKGDB2_CONFIG'] = '/etc/pkgdb2/pkgdb2.cfg'

## The following is only needed if you did not install pkgdb
## as a python module (for example if you run it from a git clone).
#import sys
#sys.path.insert(0, '/path/to/pkgdb/')


## The most import line to make the wsgi working
from pkgdb2 import APP as application


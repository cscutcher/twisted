#! /usr/bin/env python

# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
Package installer for Twisted

Copyright (c) 2001 by Twisted Matrix Laboratories
All rights reserved, see LICENSE for details.

$Id: setup.py,v 1.16 2002/03/13 22:19:28 itamarst Exp $
"""

import distutils, os, sys
from distutils.core import setup, Extension
from twisted import copyright

#############################################################################
### Call setup()
#############################################################################

setup_args = {
    'name': "Twisted",
    'version': copyright.version,
    'description': "Twisted %s is a framework to build frameworks" % (copyright.version,),
    'author': "Twisted Matrix Laboratories",
    'author_email': "twisted-python@twistedmatrix.com",
    'maintainer': "Glyph Lefkowitz",
    'maintainer_email': "glyph@twistedmatrix.com",
    'url': "http://twistedmatrix.com/",
    'licence': "GNU LGPL",
    'long_description': """
Twisted is a framework to build frameworks. It is expected that one day
the project has expanded to the point that the Twisted Reality framework
(a very small part of the codebase, even now) can seamlessly integrate
with mail, web, DNS, netnews, IRC, RDBMSs, desktop environments, and
your toaster. 
""",
    'packages': [
        "twisted",
        # "twisted.bugs",
        "twisted.coil",
        "twisted.coils",
        "twisted.cred",
        # "twisted.eco",
        "twisted.enterprise",
        # "twisted.forum",
        "twisted.im",
        "twisted.internet",
        "twisted.lumberjack",
        "twisted.mail",
        "twisted.manhole",
        "twisted.manhole.ui",
        # "twisted.metrics",
        "twisted.names",
        "twisted.persisted",
        "twisted.protocols",
        "twisted.protocols.ldap",
        "twisted.python",
        "twisted.reality",
        "twisted.reality.ui",
        "twisted.spread",
        "twisted.spread.ui",
        "twisted.tap",
        "twisted.test",
        "twisted.web",
        "twisted.words",
        "twisted.words.ui",
        "twisted.words.ui.gateways",
    ],
}

if hasattr(distutils.dist.DistributionMetadata, 'get_keywords'):
    setup_args['keywords'] = "internet www tcp framework games"

if hasattr(distutils.dist.DistributionMetadata, 'get_platforms'):
    setup_args['platforms'] = "win32 posix"

if os.name == 'posix':
    import glob
    setup_args['scripts'] = ['bin/manhole', 'bin/mktap', 'bin/gnusto', 'bin/twistd', 'bin/im', 'bin/t-im', 'bin/faucet']


# make sure data files are installed in twisted package
# this is evil.
from distutils.command.install_data import install_data

class my_install_data(install_data):
    def finalize_options (self):
        self.set_undefined_options('install',
            ('install_lib', 'install_dir'),
            ('root', 'root'),
            ('force', 'force'),
        )

imPath = os.path.join('twisted', 'im')
setup_args['data_files'] = [(imPath, [os.path.join(imPath, 'instancemessenger.glade')]),
                            ('twisted', [os.path.join('twisted', 'plugins.tml')])]
setup_args['cmdclass']=  {'install_data': my_install_data}

#'"
# for building C banana...

def extpath(path):
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), path)
    

# cBanana is currently broken

#setup_args['ext_modules'] = [
#    Extension("twisted.spread.cBanana", [extpath("twisted/spread/cBanana.c")]),
#    ]

apply(setup, (), setup_args)


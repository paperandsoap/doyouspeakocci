#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# This file is part of doyouspeakOCCI.
#
# doyouspeakOCCI is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# doyouspeakOCCI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#

from distutils.core import setup

setup(
    name = 'doyouspeakOCCI',
    version = '0.2',

    author = 'Alexander Papaspyrou',
    author_email = 'alexander.papaspyrou@tu-dortmund.de',
    maintainer = 'The doyouspeakOCCI Community',
    maintainer_email = 'doyouspeakocci@googlegroups.com',

    url='http://doyouspeakocci.appspot.com',
    description = 'A Google App Enginge based compliance test suite for the Open Cloud Computing Interface (OCCI) family of specifications.',
    long_description = 'The doyouspeakOCCI Compliance Testing Facility is a [Google App Engine (GAE)](http://code.google.com/appengine/)-based checking tool for the [Open Cloud Computing Interface (OCCI)](http://occi-wg.org/) family of specifications. More specifically, it provides a full compliance test suite for the [OCCI Core (GFD.183)](http://ogf.org/documents/GFD.183.pdf), [OCCI Infrastructure (GFD.184)](http://ogf.org/documents/GFD.184.pdf), and [OCCI RESTful HTTP Rendering (GFD.185)](http://ogf.org/documents/GFD.185.pdf) specifications.',

    download_url = 'http://github.com/irf/doyouspeakocci',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Testing',
    ],
    platforms = [
        'Google App Engine',
    ],

    packages=['dyso'],
)

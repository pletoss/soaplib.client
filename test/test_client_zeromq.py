#!/usr/bin/env python
#
# soaplib - Copyright (C) Soaplib contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

import unittest

from _test_client_base import SoaplibClientTestBase
from soaplib.client.zeromq import Client
from soaplib.test.interop.server._service import application

class TestSoaplibZmqClient(SoaplibClientTestBase,unittest.TestCase):
    def setUp(self):
        self.client = Client('tcp://localhost:5555', application)
        self.ns = "soaplib.test.interop.server._service"

if __name__ == '__main__':
    unittest.main()

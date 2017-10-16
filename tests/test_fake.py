#!/usr/bin/env python
"""
Fake test
"""
from __future__ import print_function, unicode_literals

import unittest


class TestFake(unittest.TestCase):

    def test_fake(self):
        # Just to check the option can be called with
        # nosetests for different Python versions.
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

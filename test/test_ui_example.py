# -*- coding: utf-8 -*-

import unittest

from .lib.f360_mock.create import create_object

# Required so that adsk.fusion.Component can be created
import adsk.core


class GetValueTestCase(unittest.TestCase):
    def setUp(self):
        self.value = 5
        self.undertest = create_object('adsk.core.StringValueCommandInput',
                                       {'value': lambda _: self.value})

    def test_get_value(self):
        actual = self.undertest.value
        self.assertEqual(self.value, actual)



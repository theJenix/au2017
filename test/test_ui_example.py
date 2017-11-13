# -*- coding: utf-8 -*-

import unittest

from .lib.f360_mock.create import create_object

# Required so that adsk.fusion.Component can be created
import adsk.core

from demo_component import make_demo_component_name

class GetValueTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = 'DEMO: Widget'
        self.value = 'Widget'
        self.undertest = create_object('adsk.core.StringValueCommandInput',
                                       {'value': lambda _: self.value})

    def test_get_value(self):
        actual = make_demo_component_name(self.undertest)
        self.assertEqual(self.expected, actual)



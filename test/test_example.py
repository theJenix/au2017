# -*- coding: utf-8 -*-

import unittest

from .lib.f360_mock.create import create_object

# Required so that adsk.fusion.Component can be created
import adsk.fusion


def component_histogram(c, hist):
    name = c.name
    if name not in hist:
        hist[name] = 0
    hist[name] += 1

class ComponentHistogramTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = {'foo': 2, 'bar': 1}
        self.components = [\
            create_object('adsk.fusion.Component', {'name': 'foo'}),\
            create_object('adsk.fusion.Component', {'name': 'bar'}),\
            create_object('adsk.fusion.Component', {'name': 'foo'})]

    def test_component_histogram(self):
        hist = {}
        for c in self.components:
            component_histogram(c, hist)

        self.assertDictEqual(self.expected, hist)

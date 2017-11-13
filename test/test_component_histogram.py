# -*- coding: utf-8 -*-

import unittest

from .lib.f360mock.create import create_object
from component_histogram import component_histogram


class ComponentHistogramTestCase(unittest.TestCase):
    def setUp(self):
        self.expected = {'foo': 2, 'bar': 1}
        self.components = [
            create_object('adsk.fusion.Component', {'name': 'foo'}),
            create_object('adsk.fusion.Component', {'name': 'bar'}),
            create_object('adsk.fusion.Component', {'name': 'foo'})]

    def test_component_histogram(self):
        hist = {}
        for c in self.components:
            component_histogram(c, hist)

        self.assertDictEqual(self.expected, hist)

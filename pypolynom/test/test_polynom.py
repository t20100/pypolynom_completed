# coding: utf-8

"""Unit tests for the module polynom."""

import unittest
from .. import polynom

class TestSqrt(unittest.TestCase):

    def testInteger(self):
        result = polynom.sqrt(4)
        self.assertEqual(result, 2)

    def testFloat(self):
        result = polynom.sqrt(0.5)
        self.assertAlmostEqual(result, 0.7071, places=4)

    def testNegative(self):
        with self.assertRaises(TypeError):
            result = polynom.sqrt("mmm")

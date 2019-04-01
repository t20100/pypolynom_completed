# coding: utf-8

"""Unit tests for the module math."""

import unittest
import math
from .. import math

class TestSqrt(unittest.TestCase):

    def test_integer(self):
        result = math.sqrt(4)
        self.assertEqual(result, 2)

    def test_float(self):
        result = math.sqrt(0.5)
        self.assertAlmostEqual(result, 0.7071, places=4)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = math.sqrt("mmm")


class TestPow2(unittest.TestCase):

    def test_0_roots(self):
        result = math.pow2(2)
        self.assertEqual(result, 4)

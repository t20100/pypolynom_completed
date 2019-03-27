# coding: utf-8

"""Unit tests for the module polynom."""

import unittest
import math
from .. import polynom

class TestSqrt(unittest.TestCase):

    def test_integer(self):
        result = polynom.sqrt(4)
        self.assertEqual(result, 2)

    def test_float(self):
        result = polynom.sqrt(0.5)
        self.assertAlmostEqual(result, 0.7071, places=4)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = polynom.sqrt("mmm")


class TestPolygom(unittest.TestCase):

    def test_0_roots(self):
        result = polynom.polynom(2, 0, 1)
        self.assertEqual(len(result), 0)

    def test_1_root(self):
        result = polynom.polynom(2, 0, 0)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, [0])

    def test_2_root(self):
        result = polynom.polynom(4, 0, -4)
        self.assertEqual(len(result), 2)
        result = sorted(result)
        self.assertEqual(set(result), set([-1, 1]))

    def test_float(self):
        result = polynom.polynom(math.pi, math.pi, -math.pi)
        self.assertEqual(len(result), 2)
        result = sorted(result)
        self.assertAlmostEqual(result[0], -1.6180, places=4)
        self.assertAlmostEqual(result[1], 0.6180, places=4)

    def test_not_polynom(self):
        with self.assertRaises(ValueError):
            result = polynom.polynom(0, 0, 0)


class TestPow2(unittest.TestCase):

    def test_0_roots(self):
        result = polynom.pow2(2)
        self.assertEqual(result, 4)

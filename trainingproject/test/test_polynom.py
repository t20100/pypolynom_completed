# coding: utf-8

"""Unit tests for the module polynom."""

import unittest
import math
from .. import polynom


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

    def test_value(self):
        result = polynom.polynom(math.pi, math.pi, -math.pi)
        self.assertEqual(len(result), 2)
        result = sorted(result)
        self.assertAlmostEqual(result[0], -1.6180, places=4)
        self.assertAlmostEqual(result[1], 0.6180, places=4)

    def test_many_values(self):
        tests = [
            ([4, 1, 3], []),
            ([1.2, 6.5, 1.0], [-5.25818, -0.15848]),
            ([9, 3.3, -100], [-3.52170, 3.15503]),
            ([-9.11, -8, 10.0], [-1.57507, 0.69691]),
            ]

        for test in tests:
            values, expected = test
            with self.subTest(values=values, expected=expected):
                result = polynom.polynom(*values)
                self.assertEqual(len(result), len(expected))
                result = sorted(result)
                for i in range(len(expected)):
                    self.assertAlmostEqual(result[i], expected[i], places=4)

    def test_not_polynom(self):
        with self.assertRaises(ValueError):
            result = polynom.polynom(0, 0, 0)

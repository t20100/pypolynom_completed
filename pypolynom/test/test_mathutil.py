# coding: utf-8

"""Unit tests for the module math."""

import unittest
import math
from .. import mathutil

class TestSqrt(unittest.TestCase):

    def test_integer(self):
        result = mathutil.sqrt(4)
        self.assertEqual(result, 2)

    def test_float(self):
        result = mathutil.sqrt(0.5)
        self.assertAlmostEqual(result, 0.7071, places=4)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = mathutil.sqrt("mmm")


class TestPow2(unittest.TestCase):

    def test_0_roots(self):
        result = mathutil.pow2(2)
        self.assertEqual(result, 4)


def suite():
    loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
    suite = unittest.TestSuite()
    suite.addTest(loadTests(TestSqrt))
    suite.addTest(loadTests(TestPow2))
    return suite

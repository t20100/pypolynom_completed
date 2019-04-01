# coding: utf-8

"""Unit tests for the module math."""

from PyQt5 import Qt
from PyQt5.QtTest import QTest

import unittest
import math
from .. import gui


class MockFunction(object):
    """Mock any function.

    It exists helper libraries to create mocks. Like `unittest.mock`
    or `mock`.
    """

    def __init__(self):
        self._arguments = []
        self._result = None

    def setExpectedResult(self, result):
        self._result = result

    def callCount(self):
        return len(self._arguments)

    def __call__(self, *args):
        self._arguments.append(args)
        if isinstance(self._result, Exception):
            raise self._result
        return self._result


class TestUnit(unittest.TestCase):
    """Test only the module and mock the dependancies"""

    def setUp(self):
        # Make sure Qt is initialized
        qapp = Qt.QApplication.instance()
        if Qt.QApplication.instance() is None:
            qapp = Qt.QApplication([])
        self.qapp = qapp

        # Mock the dependancies
        self._old = gui.polynom.polynom
        self._mock = MockFunction()
        gui.polynom.polynom = self._mock

        self._mockedQMessage = MockFunction()
        self._oldMessage = Qt.QMessageBox.critical
        Qt.QMessageBox.critical = self._mockedQMessage

    def tearDown(self):
        # Resitute the context
        gui.polynom.polynom = self._old
        self._old = None
        self._mock = None

        Qt.QMessageBox.critical = self._oldMessage
        self._oldMessage = None
        self._mockedQMessage = None

    def test_0_result(self):
        self._mock.setExpectedResult([])
        # Check the process
        solver = gui.PolynomSolver()
        QTest.qWaitForWindowExposed(solver)
        QTest.keyClicks(solver._inputLine, '0 1 2', delay=100)  # Wait 100ms
        QTest.mouseClick(solver._processButton, Qt.Qt.LeftButton, pos=Qt.QPoint(1, 1))
        self.assertEqual(solver._resultWidget.text(), "No solution")
        # Check the protocol
        self.assertEqual(self._mock.callCount(), 1)
        self.assertEqual(self._mock._arguments[0], (0, 1, 2))

    def _test_1_result(self):
        # It is not needed to test it. Cause it is the same coverage as test_2_result
        # Here we test the GUI, not the `polynom` function.
        pass

    def test_2_result(self):
        self._mock.setExpectedResult([0, 1])
        # Check the process
        solver = gui.PolynomSolver()
        QTest.qWaitForWindowExposed(solver)
        QTest.keyClicks(solver._inputLine, '0 1 2', delay=100)  # Wait 100ms
        QTest.mouseClick(solver._processButton, Qt.Qt.LeftButton, pos=Qt.QPoint(1, 1))
        self.assertEqual(solver._resultWidget.text(), "0.000 1.000")
        # Check the protocol
        self.assertEqual(self._mock.callCount(), 1)
        self.assertEqual(self._mock._arguments[0], (0, 1, 2))

    def test_argument_error(self):
        # Note that it can be hard to test dialogs, as we lose the hand on the
        # processing of the events. Here we have mocked the QMessage API
        solver = gui.PolynomSolver()
        QTest.qWaitForWindowExposed(solver)
        QTest.keyClicks(solver._inputLine, 'mmmm', delay=100)  # Wait 100ms
        QTest.mouseClick(solver._processButton, Qt.Qt.LeftButton, pos=Qt.QPoint(1, 1))
        # Check the protocol
        self.assertEqual(self._mock.callCount(), 0)
        self.assertEqual(self._mockedQMessage.callCount(), 1)

    def test_exception_result(self):
        # Note that it can be hard to test dialogs, as we lose the hand on the
        # processing of the events. Here we have mocked the QMessage API
        self._mock.setExpectedResult(TypeError("Mocked exception"))
        solver = gui.PolynomSolver()
        QTest.qWaitForWindowExposed(solver)
        QTest.keyClicks(solver._inputLine, '0 1 2', delay=100)  # Wait 100ms
        QTest.mouseClick(solver._processButton, Qt.Qt.LeftButton, pos=Qt.QPoint(1, 1))
        # Check the protocol
        self.assertEqual(self._mock.callCount(), 1)
        self.assertEqual(self._mockedQMessage.callCount(), 1)


class TestIntegration(unittest.TestCase):
    """Test the module with it's dependancies"""

    def setUp(self):
        # Make sure Qt is initialized
        qapp = Qt.QApplication.instance()
        if Qt.QApplication.instance() is None:
            qapp = Qt.QApplication([])
        self.qapp = qapp

    def test_integration(self):
        solver = gui.PolynomSolver()
        QTest.qWaitForWindowExposed(solver)
        QTest.keyClicks(solver._inputLine, '-2 20 -50', delay=100)  # Wait 100ms
        QTest.mouseClick(solver._processButton, Qt.Qt.LeftButton, pos=Qt.QPoint(1, 1))
        self.assertEqual(solver._resultWidget.text(), "5.000")


def suite():
    loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
    suite = unittest.TestSuite()
    suite.addTest(loadTests(TestUnit))
    suite.addTest(loadTests(TestIntegration))
    return suite

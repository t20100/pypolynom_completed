"""
Test module.

.. code-block::

    # Test the project
    python -m unittest

    # Test the project using the suite
    python -m unittest trainingproject.test.suite

    # Test coverage with percentage of coverage per module
    python -m coverage run -m unittest
    python -m coverage report

    # Test coverage with file annotation
    python -m coverage run -m unittest
    python -m coverage annotate


It also can be achived with a single command line using the `pytest` library and
extension library `pytest-cov`.

.. code-block::

    # Test the project
    python -m pytest

    # Test coverage with percentage of coverage per module
    python -m pytest --cov trainingproject

    # Test coverage with file annotation
    python3.5 -m pytest --cov trainingproject --cov-report annotate
"""

def suite_without_gui():
    import unittest
    from . import test_mathutil
    from . import test_polynom

    suite = unittest.TestSuite()
    suite.addTest(test_mathutil.suite())
    suite.addTest(test_polynom.suite())
    return suite


def suite():
    # For convinience
    return suite_without_gui()


def suite_with_gui():
    import unittest
    from . import test_gui

    suite = unittest.TestSuite()
    suite.addTest(suite_without_gui())
    suite.addTest(test_gui.suite())
    return suite

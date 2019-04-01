"""
Test module.

.. code-block::

    # Test the project
    python -m unittest

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
    python -m pytest --cov pypolynom

    # Test coverage with file annotation
    python3.5 -m pytest --cov pypolynom --cov-report annotate
"""


"""
Test module.

.. code-block::

    # Test the project
    python -m unittst

    # Test coveraage with percentage of coverage per modules
    python -m coverage run -m unittest
    python -m coverage report

    # Test coveraage with file annotation
    python -m coverage run -m unittest
    python -m coverage annotate


It also can be achived with a single command line using libraries `pytest` and
extension library `pytest-cov`.

.. code-block::

    # Test the project
    python -m pytest

    # Test coveraage with percentage of coverage per modules
    python -m pytest --cov pypolynom

    # Test coveraage with file annotation
    python3.5 -m pytest --cov pypolynom --cov-report annotate
"""

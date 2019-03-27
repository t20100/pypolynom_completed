# coding: utf-8

"""This is a simple demonstration library"""

__authors__ = ["Pierre Knobel", "Jerome Kieffer", "Pierre Palero",
               "Henri Payno", "Armando Sole", "Valentin Valls",
               "Thomas Vincent"]
__date__ = "27/03/2019"
__license__ = "MIT"


def sqrt(x):
    """Return the square root of x

    :param float x: Input value
    :rtype: float
    """
    return x**0.5


def polynom(a, b, c):
    """Solve the polygon of order two.

    :param float a: a value of the polynom
    :param float b: b value of the polynom
    :param float c: c value of the polynom
    :rtype: List[float]
    """
    if a == 0:
        # Not a polynom
        raise ValueError("Not a quadratic equation (a==0)")
    delta = pow2(b) - 4.0 * a * c
    solutions = []
    if delta > 0:
        solutions.append((-b + sqrt(delta)) / (2.0 * a))
        solutions.append((-b - sqrt(delta)) / (2.0 * a))
    elif delta == 0:
        solutions.append(-b/(2.0*a))
    return solutions


def pow2(x):
    """Return the square of x
    :param float x: input value
    :rtype: float
    """
    return x*x

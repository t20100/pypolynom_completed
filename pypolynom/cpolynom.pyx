# coding: utf-8

"""This is a simple demonstration library"""

__authors__ = ["Pierre Knobel", "Jerome Kieffer", "Pierre Palero",
               "Henri Payno", "Armando Sole", "Valentin Valls",
               "Thomas Vincent"]
__date__ = "01/04/2019"
__license__ = "MIT"


def polynom(a, b, c):
    """Solve the polygon of order two.

    .. math:: a\cdotx^2 + b\cdotx + c = 0

    :param float a: a value of the polynom
    :param float b: b value of the polynom
    :param float c: c value of the polynom
    :rtype: List[float]
    """
    if a == 0:
        # Not a polynom
        raise ValueError("Not a quadratic equation (a==0)")
    delta = (b**2.0) - 4.0 * a * c
    solutions = []
    if delta > 0:
        solutions.append((-b + (delta**0.5)) / (2.0 * a))
        solutions.append((-b - (delta**0.5)) / (2.0 * a))
    elif delta == 0:
        solutions.append(-b / (2.0 * a))
    return solutions

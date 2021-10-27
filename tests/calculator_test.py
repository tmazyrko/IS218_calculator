"""Testing the Calculator"""
from calc.main import Calculator


def test_calculator_add_static():
    """Testing """
    assert Calculator.add_numbers(1, 2) == 3

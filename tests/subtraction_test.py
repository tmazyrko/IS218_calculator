"""Testing Addition class"""
from calc.operations.subtraction import Subtraction


def test_calculator_subtract_static():
    """Tests subtraction"""
    assert Subtraction.subtract(5, 2) == 3

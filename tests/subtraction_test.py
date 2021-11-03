"""Testing Addition class"""
from calc.operations.subtraction import Subtraction


def test_calculator_subtract_static():
    """Tests subtraction"""
    subtraction = Subtraction(5, 2)
    assert subtraction.get_result() == 3

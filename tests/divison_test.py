"""Testing Division class"""
from calc.operations.division import Division


def test_calculator_subtract_static():
    """Tests division"""
    assert Division.divide(6, 2) == 3

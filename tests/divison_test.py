"""Testing Division class"""
from calc.operations.division import Division


def test_calculator_subtract_static():
    """Tests division"""
    division = Division(6, 2)
    assert division.get_result() == 3

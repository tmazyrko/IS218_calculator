"""Testing Addition class"""
from calc.operations.addition import Addition


def test_calculator_add_static():
    """Tests addition"""
    assert Addition.add(1, 2) == 3

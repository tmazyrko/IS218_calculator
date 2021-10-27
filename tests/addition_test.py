"""Testing Addition class"""
from calc.operations.addition import Addition


def test_calculator_add_static():
    assert Addition.add(1, 2) == 3

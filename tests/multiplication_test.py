"""Testing Multiplication class"""
from calc.operations.multiplication import Multiplication


def test_calculator_multiply_static():
    assert Multiplication.multiply(5, 2) == 10

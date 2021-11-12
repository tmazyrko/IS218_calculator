""" Testing Multiplication class """
from calc.operations.multiplication import Multiplication


def test_operation_multiplication():
    """ Tests multiplication """
    values = (5.0, 2.0)
    multiplication = Multiplication.create(values)
    assert multiplication.get_result() == 10.0

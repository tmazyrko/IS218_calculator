""" Testing Addition class """
from calc.operations.addition import Addition


def test_operation_addition():
    """ Tests addition """
    values = (1.0, 2.0)
    addition = Addition(values)
    assert addition.get_result() == 3.0

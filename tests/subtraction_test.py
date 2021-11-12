""" Testing Subtraction class """
from calc.operations.subtraction import Subtraction


def test_operation_subtraction():
    """ Tests subtraction """
    values = (5.0, 2.0)
    subtraction = Subtraction.create(values)
    assert subtraction.get_result() == 3.0

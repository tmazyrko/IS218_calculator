""" Testing Division class """
from calc.operations.division import Division


def test_operation_division():
    """ Tests division """
    values = (6.0, 2.0)
    division = Division.create(values)
    assert division.get_result() == 3.0

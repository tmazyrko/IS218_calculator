""" Testing the Calculator """
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():  # pylint: disable=redefined-outer-name
    """ Fixture for clearing Calculations history """
    Calculations.clear_history()


def test_calculator_add_static(clear_history_fixture):  # pylint: disable=unused-argument,redefined-outer-name
    """ Testing that the calculator has a static method for addition """
    values = (1.0, 2.0, 5.0)
    Calculator.add_numbers(values)
    assert Calculator.get_last_result_value() == 8.0


def test_calculator_subtract_static(clear_history_fixture):  # pylint: disable=unused-argument,redefined-outer-name
    """ Testing that the calculator has a static method for subtraction """
    values = (1.0, 2.0, 5.0)
    Calculator.subtract_numbers(values)
    assert Calculator.get_last_result_value() == -6.0


def test_calculator_multiply_static(clear_history_fixture):  # pylint: disable=unused-argument,redefined-outer-name
    """ Testing that the calculator has a static method for multiplication """
    values = (3.0, 2.0, 5.0)
    Calculator.multiply_numbers(values)
    assert Calculator.get_last_result_value() == 30.0


def test_calculator_divide_static(clear_history_fixture):  # pylint: disable=unused-argument,redefined-outer-name
    """ Testing that the calculator has a static method for division """
    values = (20.0, 2.0, 2.0)
    Calculator.divide_numbers(values)
    assert Calculator.get_last_result_value() == 5.0

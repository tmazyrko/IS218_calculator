""" Testing the Calculations History """
import pytest
from calc.history.calculations import Calculations
from calc.operations.addition import Addition


@pytest.fixture
def clear_history_fixture():  # pylint: disable=redefined-outer-name
    """ Fixture for clearing Calculations history """
    Calculations.clear_history()


@pytest.fixture
def setup_addition_calculation_fixture():  # pylint: disable=redefined-outer-name
    """ Fixture for setting up an Addition calculation object """
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    """ Testing that adding a calculation works """
    assert Calculations.count_history() == 1


def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    """ Testing clear history """
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True


def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting the count of calculations in history """
    assert Calculations.count_history() == 1


def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting a specific calculation out of history """
    assert Calculations.get_calculation(0).get_result() == 3


def test_get_calc_first_object(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting the first calculation obj from history """
    assert isinstance(Calculations.get_first_calculation_object(), Addition)


def test_get_calc_first_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting the result of the first calculation from history """
    assert Calculations.get_first_calculation_result() == 3


def test_get_calc_last_object(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting the last calculation obj from history """
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Addition)


def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    # pylint: disable=unused-argument,redefined-outer-name
    """ Testing getting the result of the last calculation from history """
    assert Calculations.get_last_calculation_result() == 3

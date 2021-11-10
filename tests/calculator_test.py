"""Testing the Calculator"""
from calc.calculator import Calculator


def test_calculator_add_static():
    """Testing """
    assert Calculator.add_numbers(1, 2) == 3


def test_calculator_subtract_static():
    """Testing """
    assert Calculator.subtract_numbers(5, 2) == 3


def test_calculator_multiply_static():
    """Testing """
    assert Calculator.multiply_numbers(5, 2) == 10


def test_calculator_divide_static():
    """Testing """
    assert Calculator.divide_numbers(6, 2) == 3


def test_calculator_history_static_property():
    """Testing Calculator history"""
    prev_length = len(Calculator.history)
    Calculator.add_numbers(1, 2)
    assert len(Calculator.history) == prev_length + 1


def test_calculator_history_get_addition_calculation():
    """Testing ability to get Calculator object from history"""
    calculation = Calculator.history[0]
    assert calculation.get_result() == 3


def test_calculator_history_get_length():
    """Testing method returning length of history list"""
    length = Calculator.history_length()
    assert length == 5


def test_calculator_history_get_first_obj():
    """Testing method getting first object from history"""
    assert Calculator.get_first_history_obj() == Calculator.history[0]


def test_calculator_history_get_first_result():
    """Testing method getting result of first calculation in history"""
    assert Calculator.get_first_history_result() == 3


def test_calculator_history_get_last_obj():
    """Testing method getting last object from history"""
    assert Calculator.get_last_history_obj() == Calculator.history[Calculator.history_length() - 1]


def test_calculator_history_get_last_result():
    """Testing method getting result of last calculation in history"""
    result = Calculator.add_numbers(7, 4)
    assert Calculator.get_last_history_result() == result


def test_calculator_history_remove_calculation():
    """Testing method to remove single calculation from history"""
    pre_length = Calculator.history_length()
    Calculator.history_remove(0)
    post_length = Calculator.history_length()
    assert post_length == pre_length - 1


def test_calculator_clear_history():
    """Testing clear history method"""
    Calculator.clear_history()
    length = Calculator.history_length()
    assert length == 0

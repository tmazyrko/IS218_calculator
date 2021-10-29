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

"""Multiplication Class"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Multiplication class"""

    def get_result(self):
        """Returns multiple of two numbers"""
        return self.value_a * self.value_b

"""Subtraction Class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """Subtraction class"""

    def get_result(self):
        """Returns difference between two numbers"""
        return self.value_a - self.value_b

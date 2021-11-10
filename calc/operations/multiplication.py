"""Multiplication Class"""
from calc.operations.operation import Operation


class Multiplication(Operation):  # pylint: disable=too-few-public-methods
    """Multiplication class"""

    def get_result(self):
        """Returns multiple of two numbers"""
        result = self.values[0]
        for val in self.values[1:]:
            result *= val
        return result

"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):  # pylint: disable=too-few-public-methods
    """Addition class"""

    def get_result(self):
        """Returns sum of two numbers"""
        return self.value_a + self.value_b

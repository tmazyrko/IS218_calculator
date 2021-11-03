"""Division Class"""
from calc.operations.calculation import Calculation


class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Division class"""

    def get_result(self):
        """Returns division result of two numbers"""
        return self.value_a / self.value_b

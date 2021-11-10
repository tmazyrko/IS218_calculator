"""Division Class"""
from calc.operations.operation import Operation


class Division(Operation):  # pylint: disable=too-few-public-methods
    """Division class"""

    def get_result(self):
        """Returns division result of two numbers"""
        result = self.values[0]
        for val in self.values[1:]:
            result /= val
        return result

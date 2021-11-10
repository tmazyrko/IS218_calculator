"""Addition Class"""
from calc.operations.operation import Operation


class Addition(Operation):  # pylint: disable=too-few-public-methods
    """Addition class"""

    def get_result(self):
        """Returns sum of two numbers"""
        result = self.values[0]
        for val in self.values[1:]:
            result += val
        return result

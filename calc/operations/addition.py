"""Addition Class"""


class Addition:  # pylint: disable=too-few-public-methods
    """Addition class"""

    def __init__(self, value_a, value_b):
        """Default constructor"""
        self.value_a = value_a
        self.value_b = value_b

    def get_result(self):
        """Returns sum of two numbers"""
        return self.value_a + self.value_b

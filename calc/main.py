""" Main calc module """
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ returns sum of two numbers """
        return Addition.add(value_a, value_b)

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_number(self, value_a):
        """ multiply number by result """
        self.result = self.result * value_a
        return self.result

    def divide_number(self, value_a):
        """ divide result by number """
        try:
            self.result = self.result / value_a
            return self.result
        except ZeroDivisionError:
            print('Cannot divide by zero!')
            return 0

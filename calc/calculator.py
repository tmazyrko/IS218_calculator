""" Main calc module """
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ returns sum of two numbers """
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ returns difference of two numbers """
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ returns multiple of two numbers """
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ returns division result of two numbers """
        return Division.divide(value_a, value_b)

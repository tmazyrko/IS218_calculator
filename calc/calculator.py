""" Main calc module """
from calc.history.calculations import Calculations


class Calculator:
    """ Calculator class calls methods on the Calculations class """

    @staticmethod
    def add_numbers(value_a, value_b):
        """ returns sum of two numbers """
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ returns difference of two numbers """
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ returns multiple of two numbers """
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ returns division result of two numbers """
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.get_result()

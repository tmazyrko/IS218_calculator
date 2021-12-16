""" Main calc module """
from calc.history.calculations import Calculations


class Calculator:
    """ Calculator class calls methods on the Calculations class """

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ returns sum of numbers """
        Calculations.add_calculation_addition(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ returns difference of numbers """
        Calculations.add_calculation_subtraction(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ returns multiple of numbers """
        Calculations.add_calculation_multiplication(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ returns division result of numbers """
        Calculations.add_calculation_division(tuple_values)
        return True

    @staticmethod
    def get_last_result_value():
        """ gets the result of the calculation """
        return Calculations.get_last_calculation_result()

    @staticmethod
    def history_as_list_of_dicts():
        """ gets calculation history as a list of dictionaries """
        return Calculations.to_list_of_dicts()

""" Operation Class """


class Operation:  # pylint: disable=too-few-public-methods
    """ Operation abstract base class """

    def __init__(self, values: tuple):
        """ Default constructor """
        self.values = Operation.convert_args_to_tuple_of_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ Factory method """
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ Standardizes values to a list of floats """
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)

""" Operation Class """
import datetime
import pytz


class Operation:  # pylint: disable=too-few-public-methods
    """ Operation abstract base class """

    def __init__(self, values: tuple):
        """ Default constructor """
        self.tz = 'America/New_York'  # US East timezone
        self.values = Operation.convert_args_to_tuple_of_float(values)
        self.timestamp = self.set_timestamp(self.tz)

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

    @staticmethod
    def set_timestamp(tz):
        """ Returns a formatted timestamp for the creation of an operation """
        timestamp = datetime.datetime.now(pytz.timezone(tz))
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S (UTC%z)")
        return formatted_timestamp

    def get_timestamp(self):
        """ Retrieves stored timestamp """
        return self.timestamp

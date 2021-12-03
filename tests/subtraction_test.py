""" Testing Subtraction class """
import pandas as pd
from calc.operations.subtraction import Subtraction


def test_operation_subtraction():
    """ Tests subtraction """
    values = (5.0, 2.0)
    subtraction = Subtraction.create(values)
    assert subtraction.get_result() == 3.0


def test_operation_subtraction_csv():
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    """ Tests subtraction, uses csv file for input data """
    input_file = "subtraction_test_small.csv"
    full_path = "tests/input_data/" + input_file
    dataframe = pd.read_csv(full_path)
    for index, row in dataframe.iterrows():
        subtraction = Subtraction.create((row['value a'], row['value b']))
        assert subtraction.get_result() == float(row['answer'])

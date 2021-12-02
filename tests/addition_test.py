""" Testing Addition class """
import pandas as pd
from calc.operations.addition import Addition


def test_operation_addition():
    """ Tests addition """
    values = (1.0, 2.0)
    addition = Addition.create(values)
    assert addition.get_result() == 3.0


def test_operation_addition_csv():
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    """ Tests addition, uses csv file for input data """
    input_file = "addition_test_small.csv"
    full_path = "tests/input_data/" + input_file
    dataframe = pd.read_csv(full_path)
    for index, row in dataframe.iterrows():
        addition = Addition.create((row['value a'], row['value b']))
        assert addition.get_result() == float(row['answer'])

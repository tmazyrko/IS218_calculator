""" Testing Multiplication class """
import pandas as pd
from calc.operations.multiplication import Multiplication


def test_operation_multiplication():
    """ Tests multiplication """
    values = (5.0, 2.0)
    multiplication = Multiplication.create(values)
    assert multiplication.get_result() == 10.0


def test_operation_multiplication_csv():
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    """ Tests multiplication, uses csv file for input data """
    input_file = "multiplication_test_small.csv"
    full_path = "tests/input_data/" + input_file
    dataframe = pd.read_csv(full_path)
    for index, row in dataframe.iterrows():
        multiplication = Multiplication.create((row['value a'], row['value b']))
        assert multiplication.get_result() == float(row['answer'])

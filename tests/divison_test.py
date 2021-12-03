""" Testing Division class """
import pandas as pd
from calc.operations.division import Division


def test_operation_division():
    """ Tests division """
    values = (6.0, 2.0)
    division = Division.create(values)
    assert division.get_result() == 3.0


def test_divide_by_zero():
    """ Tests zero division error handling """
    values = (10.0, 0.0)
    division = Division.create(values)
    assert division.get_result() == "error"


def test_operation_division_csv():
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    """ Tests division, uses csv file for input data """
    input_file = "division_test_small.csv"
    full_path = "tests/input_data/" + input_file
    dataframe = pd.read_csv(full_path)
    for index, row in dataframe.iterrows():
        division = Division.create((row['value a'], row['value b']))
        assert division.get_result() == float(row['answer'])

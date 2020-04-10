
from cognito.check import Check
from cognito.table import Table
import os
import pytest
import pandas as pd
import numpy as np
from os import path 


def test_is_working():
    check = Check()
    print(check.is_working())

def test_is_categorical_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_categorical(df['Location']) == True

def test_is_continuous_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['Location']) != True

def test_is_continuous_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['population']) == True

def test_is_discrete_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['crime']) == True

def test_is_discrete_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['nonwhite']) != True

def test_is_discrete_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['Location']) == False

def test_is_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['density']) == False

def test_is_identifier_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['crime']) == False

def test_is_identifier_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['nonwhite']) == False

def test_is_missing_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['Location']) != True

def test_is_missing_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['population']) == True

def test_is_missing_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['nonwhite']) != True

def test_is_missing_4():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['density']) == True

def test_is_missing_5():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['crime']) != True

def test_ignore_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert list(check.ignore_identifier(df).columns) == ['population', 'nonwhite', 'density', 'crime']

def test_ignore_identifier_2():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check=Check()
    assert list(check.ignore_identifier(df).columns) == ['genus', 'vore', 'order', 'conservation', 'sleep_total', 'sleep_rem', 'sleep_cycle', 'awake', 'brainwt', 'bodywt']

def test_is_outlier_1():
    samples=[322,322,336,345,351,370,390,404,409,411,436,437,-7,80000000,789654123,0]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == [789654123]

def test_is_outlier_2():
    samples=[322,322,336,345,351,370,390,404,409,411,436,437,-7,80000000,789654123,0]
    x=pd.Series(samples)
    assert Check.is_outlier(x,5) == []

def test_is_outlier_3():
    samples=[4551,7875,931,1322,7795,22005,78,95,9874,12365]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == []

def test_is_outlier_4():
    samples=[4551,7875,931,1322,7795,22005,78,95,9874,12365]
    x=pd.Series(samples)
    assert Check.is_outlier(x,2) == [22005]

def test_is_outlier_5():
    samples=[30,171,184,201,212,250,265,270,272,289,305,306,100000,8,5,2000]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == [100000]

def test_is_outlier_6():
    samples=[30,171,184,201,212,250,265,270,272,289,305,306,100000,8,5,2000]
    x=pd.Series(samples)
    assert Check.is_outlier(x,5) == []

def test_percentage_missing_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.percentage_missing(df) == {'Location': 0.0, 'population': 9.09, 'nonwhite': 0.0, 'density': 9.09, 'crime': 0.0}

def test_percentage_missing_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check=Check()
    assert check.percentage_missing(df) == {'name': 0.0, 'genus': 0.0, 'vore': 8.43, 'order': 0.0, 'conservation': 34.94, 'sleep_total': 0.0, 'sleep_rem': 26.51, 'sleep_cycle': 61.45, 'awake': 0.0, 'brainwt': 32.53, 'bodywt': 0.0}

def test_remove_columns_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert list(check.remove_columns(df).columns) == ['Location', 'population', 'nonwhite', 'density', 'crime']

def test_remove_columns_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check = Check()
    assert list(check.remove_columns(df).columns) == ['name', 'genus', 'vore', 'order', 'conservation', 'sleep_total', 'sleep_rem', 'awake', 'brainwt', 'bodywt']

def test_remove_records_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert len(check.remove_records(df)) == 110

def test_remove_records_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check = Check()
    assert len(check.remove_records(df)) == 61

def test_encoding_categorical_1():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert check.encoding_categorical(df['mfr']) == ([1, 2, 0, 0, 3, 1], {1: 'Q', 2: 'K', 0: 'N', 3: 'K'})

def test_encoding_categorical_2():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert check.encoding_categorical(df['sex']) == ([0, 0, 0, 0, 0, 1, 1, 0], {0: 'F', 1: 'F'})

def test_encoding_categorical_3():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert check.encoding_categorical(df['Mjob']) == ([0, 0, 0, 1, 2, 3, 2, 2], {0: 'at_home', 1: 'at_home', 2: 'at_home', 3: 'health'})



def test_load_table():
    table = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    print(table.columns())

def test_table_columns_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.columns().tolist() == ['name', 'mfr', 'sodium', 'type', 'calories', 'sugars']

def test_table_columns_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.columns().tolist() == ['sex', 'age', 'Mjob', 'G1']

def test_table_total_columns_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.total_columns() == 6

def test_table_total_columns_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.total_columns() == 4

def test_table_total_columns_three():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.total_columns() == 5

def test_table_total_rows_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.total_rows() == 6

def test_table_total_rows_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.total_rows() == 110

def test_table_total_rows_three():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.total_rows() == 8

def test_table_get_categorical_1():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert list(data.get_categorical().columns) == ['Location']

def test_table_get_categorical_2():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert list(data.get_categorical().columns) == ['name', 'genus', 'vore', 'order', 'conservation']
    
def test_table_get_categorical_3():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert list(data.get_categorical().columns) == ['name', 'mfr', 'type']

def test_table_get_numerical_1():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert list(data.get_numerical().columns) == ['population', 'nonwhite', 'density', 'crime']

def test_table_get_numerical_2():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert list(data.get_numerical().columns) == ['sleep_total', 'sleep_rem', 'sleep_cycle', 'awake', 'brainwt', 'bodywt']

def test_table_get_numerical_3():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert list(data.get_numerical().columns) == ['sodium', 'calories', 'sugars']

def test_table_odd_rows_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert len(data.odd_rows()) == 55

def test_table_odd_rows_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert len(data.odd_rows()) == 41

def test_table_even_rows_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert len(data.even_rows()) == 54

def test_table_even_rows_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert len(data.even_rows()) == 41

def test_table_hot_encoder_categorical_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert len(data.hot_encoder_categorical('Location')) == len(data.data)

def test_table_hot_encoder_categorical_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert len(data.hot_encoder_categorical('name')) == len(data.data)

def test_table_convert_to_bin_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.convert_to_bin('population') == [(270, 1397), (1398, 2525), (2526, 3653), (3654, 4781), (4782, 5909), (5910, 7037), (7038, 8165), (8166, 9293), (9294, 10421), (10422, 11549), (11550, 12677)]

def test_table_convert_to_bin_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert data.convert_to_bin('bodywt') == [(0, 738), (739, 1477), (1478, 2216), (2217, 2955), (2956, 3694), (3695, 4433), (4434, 5172), (5173, 5911), (5912, 6650), (6651, 7389)]

def test_table_slice_1():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert list(data.slice(['population','density', 'crime']).columns) == ['population', 'density', 'crime']

def test_table_slice_2():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert list(data.slice(['Location','population']).columns) == ['Location', 'population']

def test_table_slice_3():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert list(data.slice(['Mjob','age']).columns) == ['Mjob', 'age']

def test_table_fix_outlier_with_std_deviation_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_test_cases.csv'))
    assert data.fix_outlier_with_std_deviation('crime').equals(data1['fix_outlier_with_std_deviation_crime']) == True

def test_table_fix_outlier_with_std_deviation_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot_test_cases.csv'))
    assert data.fix_outlier_with_std_deviation('bodywt').equals(data1['fix_outlier_with_std_deviation_bodywt']) == True

def test_table_fix_missing_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_test_cases.csv'))
    assert data.fix_missing('population').equals(data1['fix_missing_population']) == True

def test_table_fix_missing_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_test_cases.csv'))
    assert data.fix_missing('density').equals(data1['fix_missing_density']) == True

def test_table_imputer_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_test_cases.csv'))
    assert data.imputer('population', 1000).astype(np.int64).equals(data1['imputer_population']) == True

def test_table_imputer_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_test_cases.csv'))
    assert data.imputer('density', 800).astype(np.int64).equals(data1['imputer_density']) == True

def test_table_ignore_cardinal_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert list(data.ignore_cardinal().columns) == ['mfr', 'type', 'calories', 'sugars']

def test_table_ignore_cardinal_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert list(data.ignore_cardinal().columns) == ['population', 'nonwhite', 'density', 'crime']

def test_table_list_cardinal_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.list_cardinal() == ['Location']

def test_table_list_cardinal_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    assert data.list_cardinal() == ['name']

def test_table_list_cardinal_3():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.list_cardinal() == ['name', 'sodium']
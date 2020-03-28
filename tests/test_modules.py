
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


def test_is_categorical():
    """
    Check if the given dataset given a columns
    is categorical or not. 
    
    :raises     AssertionError:  { exception_description }
    """
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_categorical(df['Location']) == True

def test_load_table():
    table = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    print(table.columns())

def test_is_outlier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    print(check.is_outlier(df['crime'],3))

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


def test_is_continuous():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['Location']) != True

def test_is_identifier_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['density']) == False

def test_is_identifier_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['crime']) == False

def test_is_identifier_4():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['nonwhite']) == False

def test_ignore_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    df1= pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'ignore_identifier.csv'))
    check=Check()
    assert check.ignore_identifier(df).equals(df1)==False

def test_ignore_identifier_2():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'vgsales.csv'))
    df1= pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'vgsales_ignore_identifier.csv'))
    check=Check()
    assert check.ignore_identifier(df).equals(df1)==False
     

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

def test_is_continuous_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['population']) == True

def test_ignore_identifier_3():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check=Check()
    print(check.ignore_identifier(df))
  
def test_total_rows_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.total_rows() == 6

def test_total_rows_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.total_rows() == 110

def test_total_rows_three():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.total_rows() == 8

def test_columns_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.columns().tolist() == ['name', 'mfr', 'sodium', 'type', 'calories', 'sugars']

def test_columns_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.columns().tolist() == ['sex', 'age', 'Mjob', 'G1']


def test_total_columns_one():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert data.total_columns() == 6

def test_total_columns_two():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'))
    assert data.total_columns() == 4

def test_total_columns_three():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert data.total_columns() == 5


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

def test_remove_columns():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    df1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_remove_columns.csv'))
    check = Check()
    assert check.remove_columns(df).equals(df1) == True

def test_remove_records():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    df1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_remove_records.csv'))
    check = Check()
    assert check.remove_records(df).equals(df1) == True

def test_table_odd_rows():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_odd_rows.csv'))
    assert len(data.odd_rows()) == len(data1)

def test_table_summary():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    print(df.summary())
    df1= pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ignore_identifier.csv'))
    assert check.ignore_identifier(df).equals(df1)==False
    
def test_get_categorical_1():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data2=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_get_categorical.csv'))
    assert data.get_categorical().equals(data2)==False

def test_get_categorical_2():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    data2=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_get_categorical.csv'))
    assert data.get_categorical().equals(data2)==False
    
def test_get_categorical_3():
    data=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    data2=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal_get_categorical.csv'))
    assert data.get_categorical().equals(data2)==False
    
def test_table_summary():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    print(df.summary())

def test_correlation():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    print(df.correlation())

def test_hot_encoder_categorical_1():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert df.hot_encoder_categorical('Location').equals(df)== False
def test_hot_encoder_categorical_2():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert df.hot_encoder_categorical('name').equals(df)== False
def test_ignore_cardinal_1():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    assert df.ignore_cardinal().equals(df)== False
def test_ignore_cardinal_2():
    df=Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    assert df.ignore_cardinal().equals(df)== False


def test_table_imputer_1():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_imputer1.csv'))
    assert data.imputer('population', 1000).equals(data1['population']) == True

def test_table_imputer_2():
    data = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    data1 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman_imputer2.csv'))
    assert data.imputer('density', 800).equals(data1['density']) == True


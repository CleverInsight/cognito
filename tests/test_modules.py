from cognito.modules import Check
from cognito.data import Table
import os
import pytest
import pandas as pd
import numpy as np



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

def test_is_not_categorical():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_categorical(df['crime']) == False

def test_is_not_categorical_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_categorical(df['density']) == False


def test_sum_one():
    assert Check.sum(10, 20) == 30

def test_sum_two():
    assert Check.sum(100, 200) != 30

def test_sum_three():
    assert Check.sum(100, 100) == 200

def test_is_not_discrete_one():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['crime']) == True

def test_is_not_discrete_two():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['nonwhite']) != True

def test_is_not_discrete_three():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_discrete(df['Location']) == False

def test_encoding_column_one():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'cereal.csv'))
    print( check.encoding_categorical(df['mfr']))

def test_encoding_column_two():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'), sep=";")
    print( check.encoding_categorical(df['sex']))

def test_encoding_column_three():
    check = Check()
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'student.csv'), sep=";")
    print( check.encoding_categorical(df['Mjob']))
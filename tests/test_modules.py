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
<<<<<<< HEAD
def test_is_not_catogorial():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_categorical(df['density']) == False
def test_is_not_identifier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['Location']) == True
def test_is_not_identifier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['density']) == False
def test_is_not_identifier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['crime']) == False
def test_is_not_identifier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['nonwhite']) == False
=======

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
>>>>>>> e56911df4dcc87d3b36e641d2376f33306a18246

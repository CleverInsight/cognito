
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


def test_is_outlier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    print(check.is_outlier(df['crime']))

def test_is_outlier1():
    samples=[322,322,336,345,351,370,390,404,409,411,436,437,-7,80000000,789654123,0]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == [789654123]

def test_no_outlier1():
    samples=[322,322,336,345,351,370,390,404,409,411,436,437,-7,80000000,789654123,0]
    x=pd.Series(samples)
    assert Check.is_outlier(x,5) == []

def test_no_outlier2():
    samples=[4551,7875,931,1322,7795,22005,78,95,9874,12365]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == []

def test__is_outlier2():
    samples=[4551,7875,931,1322,7795,22005,78,95,9874,12365]
    x=pd.Series(samples)
    assert Check.is_outlier(x,2) == [22005]

def test__is_outlier3():
    samples=[30,171,184,201,212,250,265,270,272,289,305,306,100000,8,5,2000]
    x=pd.Series(samples)
    assert Check.is_outlier(x,3) == [100000]

def test__no_outlier3():
    samples=[30,171,184,201,212,250,265,270,272,289,305,306,100000,8,5,2000]
    x=pd.Series(samples)
    assert Check.is_outlier(x,5) == []

def test_is_missing_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['Location']) != True


def test_is_missing_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['population']) != True


def test_is_not_continuous():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['nonwhite']) == True

def test_is_not_continuous_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['density']) == False

def test_is_not_continuous_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_continuous(df['population']) == False


def test_is_missing_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['nonwhite']) != True


def test_is_missing_4():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['density']) != True


def test_is_missing_5():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['crime']) != True


def test_percentage_missing():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.percentage_missing(df) == {'Location': 0.0, 'population': 0.0, 'nonwhite': 0.0, 'density': 0.0, 'crime': 0.0}


from cognito.modules import Check
from cognito.data import Table
import os
import pytest
import pandas as pd
import numpy as np



def test_is_working():
    check = Check()
    print(check.is_working())


def test_load_table():
    table = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    print(table.columns())


def test_is_outlier():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    print(check.is_outlier(df['crime']))

<<<<<<< HEAD
def test_load_table():
    table = Table(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    print(table.columns())

def test_is_not_catogorial():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_categorical(df['density']) == False

def test_is_not_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['Location']) == True
=======
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
    assert check.is_missing(df['population']) == True
>>>>>>> b3e15ece856a5ac304b612658776a08ec5ba7ce1

def test_is_not_identifier_2():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['density']) == False

def test_is_not_identifier_3():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['crime']) == False

<<<<<<< HEAD
def test_is_not_identifier_4():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['nonwhite']) == False

def test_ignore_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    print(check.ignore_identifier(df))

def test_ignore_identifier_2():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'vgsales.csv'))
    check=Check()
    print(check.ignore_identifier(df))

def test_ignore_identifier_3():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'msleep_ggplot.csv'))
    check=Check()
    print(check.ignore_identifier(df))
=======
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
    assert check.is_missing(df['density']) == True



def test_is_missing_5():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    assert check.is_missing(df['crime']) != True


def test_perc_missing():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check = Check()
    check.percentage_missing(df)
>>>>>>> b3e15ece856a5ac304b612658776a08ec5ba7ce1

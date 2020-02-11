
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

def test_is_identifier_1():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'Freedman.csv'))
    check=Check()
    assert check.is_identifier(df['Location']) == True

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
 
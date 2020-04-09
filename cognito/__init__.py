# cognito
from __future__ import print_function
import os
import sys
import math
import re
from datetime import datetime
from os import path
import pandas as pd
import numpy as np
import datefinder


def is_working(column="Cognito!"):
    """
    Determines whether the specified command is working.
    :param      column:  The column
    :type       column:  string
    """
    return "Hello, %s! How are you %s?"%(column, column)


def is_categorical(column):
    """
    Determines whether the specified col is categorical.

    :param      col:  column name
    :type       col:  { pandas.series | list | tuple }
    :return     boolean: True | False

    Usage:
    ======
        >> is_categorical(data['Age'])
        >> True
    """
    try:
        return bool(True) if column.dtypes == 'object' else bool(False)

    except AttributeError:

        print("Method only supported pandas.cores.series")


def is_continuous(column):
    """
    Determines whether the specified col is continuous.

    :param      col:  column name
    :type       col:  { pandas.series | list | tuple }
    :return     boolean: True | False

    Usage:
    ======
        >> is_continuous(data['Age'])
        >> False
    """
    try:
        return bool(True) if column.dtypes == 'float64' else bool(False)

    except AttributeError:

        print("Method only supported pandas.cores.series")


def is_discrete(column):
    """
    Determines whether the specified column is discrete.

    :param      column:  column name
    :type       column:  { pandas.series | list | tuple }
    :return     boolean: True | False

    Usage:
    ======
        >> is_discrete(data['Age'])
        >> True
    """
    try:
        return bool(True) if column.dtypes == 'int64' else bool(False)

    except AttributeError:

        print("Method only supported pandas.cores.series")


def is_identifier(column):
    """
    Determines whether the specified column is identifier.

    :param      column:  The column
    :type       column:  { pandas.series | list | tuple }
    :return     boolean: True | False

    Usage:
    ======
        >> is_identifier(data['Age'])
        >> True

    """
    try:
        return bool(True) if column.nunique() == column.shape[0] else bool(False)

    except AttributeError:

        print("Method only supported pandas.cores.series")


def is_missing(column):
    """
    Determines whether the specified column has missing values.

    :param      column:  The column
    :type       column:  { pandas.series | list | tuple }
    :return     boolean: True | False

    Usage:
    ======
        >> is_missing(data['population'])
        >> True

    """
    try:
        return bool(True) if column.isnull().values.any() == bool(True) else bool(False)

    except AttributeError:

        print("Method only supported pandas.cores.series")


def ignore_identifier(dataframe):
    """
    Drops the table if the column is an identifier.

    :param      column:  The column
    :type       column:  { pandas.series | list | tuple }
    :return     DataFrame:Updated DataFrame

    Usage:
    ======
        >> ignore_identifier(data)
        >> Updated Dataframe
    """
    col = list(dataframe)
    for i in col:
        if is_identifier(dataframe[i]):
            dataframe.drop([i], axis=1, inplace=True)
    return dataframe


def is_outlier(column, threshold):
    """
    Returns all the outliers in the column.

    :param      column:   The column
    :type       column:   {pandas.series | list | tuple}
    :return     list:     List of all the ouliers in the column

    Usage:
    =====
       >> is_outlier(data['population'])
       >> [6815.0, 6860.0, 11551.0]
    """
    column = pd.Series(column)
    outliers = []
    mean = np.mean(column)
    std_dev = np.std(column)
    for value in column:
        z_score = (value - mean) / std_dev
        if np.abs(z_score) > threshold:
            outliers.append(value)
    return outliers


def percentage_missing(dataframe):
    """
    Calculates the percentage of missing value in each column of dataframe.

    :param       dataframe:  The dataframe
    :type        dataframe:  { pandas.dataframe }
    :return      dictionary:  Dictionary of column name with percentage of missing values

    Usage:
    ======
    >> percentage_missing(data)
    >> {Price:0.00, Age:10.00}

    """
    missing = dataframe.isnull().sum()
    row_size = len(dataframe.index)
    missing_dict = {}
    for i in list(dataframe.columns):
        perc = round(missing[i] / row_size * 100.0, 2)
        missing_dict.update({i:perc})
    return missing_dict


def remove_columns(dataframe):
    """
    Removes the column containing 60% or more missing data.

    :param      dataframe:  The dataframe
    :type       dataframe:  { pandas.dataframe }
    :return     dataframe:  Dataframe with the columns dropped

    Usage:
    ======
    >>remove_columns(data)
    >>dataframe

    """
    missing_dict = percentage_missing(dataframe)
    for column in missing_dict:
        if missing_dict[column] >= 60.00:
            dataframe.drop([column], axis=1, inplace=True)
    return dataframe

def remove_records(dataframe):
    """
    Removes the rows where if a column has 20 % to 30 % of missing data.

    :param      dataframe:  The dataframe
    :type       dataframe:  { pandas.dataframe }
    :return     dataframe:  Dataframe with the rows dropped

    Usage:
    ======
    >>remove_records(data)
    >>dataframe

    """
    missing_dict = percentage_missing(dataframe)
    for column in missing_dict:
        if missing_dict[column] >= 20.00 and missing_dict[column] < 30.00:
            dataframe = dataframe[dataframe[column].isnull() != bool(True)]
    return dataframe


def encoding_categorical(column):
    """
    Gives the encoding of a categorical column.

    :param      col:  column name
    :type       col:  { pandas.series | list | tuple }
    :return     list: List of updated column and dict: dictionary of encoded values
    Usage:
    ======
        >> encoding_categorical(data['Age'])
        >> False
    """
    encoded = column.astype('category').cat.codes
    encoded_col = list(encoded)
    describe_encoding = pd.Series(column, index=encoded_col).to_dict()
    return encoded_col, describe_encoding


def replace_mean(column):
    """
    Replaces the missing values of a column with its mean.

    :param       column:  The column
    :type        column:  { pandas.series | list | tuple }
    :return      column:  Updated column after replacing missing values with mean

    Usage:
    ======
    >> replace_mean(data['population'])
    >> series
    """
    try:
        return column.fillna(column.mean())

    except AttributeError:

        print("Method only supported pandas.cores.series")


def replace_mode(column):
    """
    Replaces the missing values of a column with its mode.

    :param       column:  The column
    :type        column:  { pandas.series | list | tuple }
    :return      column:  Updated column after replacing missing values with mean

    Usage:
    ======
    >> replace_mode(data['population'])
    >> series
    """
    try:
        return column.fillna(column.mode()[0])

    except AttributeError:

        print("Method only supported pandas.cores.series")


def replace_median(column):
    """
    Replaces the missing values of a column with its median.

    :param       column:  The column
    :type        column:  { pandas.series | list | tuple }
    :return      column:  Updated column after replacing missing values with median

    Usage:
    ======
    >> replace_median(data['population'])
    >> series
    """
    try:
        return column.fillna(column.median())

    except AttributeError:

        print("Method only supported pandas.cores.series")


def is_date(date):
    """
    Determines whether the specified `x` is date.

    :param      x:    string of date type
    :type       x:    string
    :returns    True | False
    Usage:
    ======
        >> is_date("20-20-2020")
        >> True

    """
    date_patterns = ["%m-%d-%Y", "%d-%m-%Y", "%Y-%m-%d"]
    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(date, pattern).date()
        except ValueError:
            return False

def is_datetime(date):
    """
    Determines whether the specified `x` is datetime.

    :param      x:    { parameter_description }
    :type       x:    { type_description }
    :returns    True | False

    Usage:
    ======
        >> is_datetime("2020-02-20 00:00:00")
        >> True
        >> is_datetime("2020-02-01")
        >> False

    """
    matches = datefinder.find_dates(date)
    for match in matches:
        if(match.hour > 0 and match.minute > 0 and match.second > 0):
            return True

    return False


def list_diff(l1, l2):
	"""
	Get the difference between two list `l1` and `l2`
	
	:param      l1:   The l 1
	:type       l1:   { type_description }
	:param      l2:   The l 2
	:type       l2:   { type_description }
	
	:returns:   { description_of_the_return_value }
	:rtype:     { return_type_description }
	"""
	return (list(set(l1) - set(l2))) 
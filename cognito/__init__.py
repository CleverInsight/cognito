# -*- coding: utf-8 -*-
from __future__ import print_function
import os, glob
import sys
import math
import re
import click
import pickle
from datetime import datetime
from os import path
import pandas as pd
import numpy as np
import datefinder
from cognito.table import Table
from tqdm import tqdm
from prettytable import PrettyTable




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


def column_missing_percentage(col):
    """
    Column missing percentage
    
    :param      col:  The col
    :type       col:  { type_description }
    
    :returns:   { description_of_the_return_value }
    :rtype:     { return_type_description }
    """
    return col.isnull().sum() * 100 / len(col)


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



def distinct_count(col):
    """
    Count the distinct values
    
    :param      col:  The col
    :type       col:  { type_description }
    
    :returns:   { description_of_the_return_value }
    :rtype:     { return_type_description }
    """
    return len(col.value_counts())


def count_min(col):

    if is_continuous(col):
        return col.min()
    else:
        return "🍋"

def count_max(col):

    if is_continuous(col):
        return col.max()
    else:
        return "🍋"

def count_mean(col):

    if is_continuous(col):
        return round(col.mean(), 2)
    else:
        return "🍋"


def count_categorical(df):
    count = 0
    for col in df.columns:
        if is_categorical(df[col]):
            count = count + 1
    return count

def count_continuous(df):
    count = 0
    for col in df.columns:
        if is_continuous(df[col]):
            count = count + 1
    return count



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


def col_missing_percentage(df, col):
    """
    Column wise missing value percentagle
    
    :param      df:   { parameter_description }
    :type       df:   { type_description }
    :param      col:  The col
    :type       col:  { type_description }
    """
    return df[col].isnull().sum() * 100 / len(df)


def type_of_variable(col):
    """
    Get type of variable
    
    :param      col:  The col
    :type       col:  { type_description }
    """
    if is_categorical(col):
        return 'categorical'

    elif is_continuous(col):
        return 'numerical'

    elif is_discrete(col):
        return 'discrete'

    elif is_identifier(col):
        return 'cardinal'

    elif is_datetime(col):
        return 'datetime'

    else:
        return col.dtypes


def check_outlier(col):
    """
    Check the outlier for the given column
    
    :param      col:  The col
    :type       col:  { type_description }
    """
    if is_continuous(col):
        if is_outlier(col, 3):
            # return "❌"
            return "🚩"
        else:
            # return "☘"
            return "✅"
          
    else:
        return "🍋"


def check_missing(col):

    if is_missing(col):
        return "🔴"
    else:
        # return "☘"
        return "✅"



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


def get_all_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    return files


def save_to(path, df, encoder):
    """
    Save the encoded dataframe to csv file and 
    picle file.
    
    :param      path:     The path
    :type       path:     { type_description }
    :param      df:       { parameter_description }
    :type       df:       { type_description }
    :param      encoder:  The encoder
    :type       encoder:  { type_description }
    """
    filename = os.path.basename(path)

    if '.' in filename:
        fname, ext = filename.split('.')
    else:
        fname = filename

    path = os.path.dirname(path)
    save_path = os.path.join(path, fname)

    # make directory
    try:
        os.mkdir(save_path)

        #filenames
        pkl_file = os.path.join(save_path, filename + '.pkl')

        if '.csv' not in filename:
            filename = filename + '.csv'    

        df_file = os.path.join(save_path, filename)

        df.to_csv(df_file, index=False)
        f = open(pkl_file, "wb")
        pickle.dump(encoder, f)
        f.close()
        return df

    except Exception as e:

        click.echo(
            click.style(
                "Abort: The {} file already exists.", fg="red"
            ).format(os.path.join(save_path, filename)), err=True)



def inverse_transform():
    """
    Inverse transform pickled encoders and output dataframe to 
    its original form.
    """
    pickles = glob.glob("*.pkl")
    datasets = glob.glob("*.csv")

    if len(pickles) > 0 and len(datasets) > 0:
        
        # pick the first pickle 
        first_pickle = pickles.pop(0)

        # Get the file related the given pickle
        fname = re.sub("\.csv\..*","", first_pickle)

        # Grab the encoder from pickle
        encoder = pickle.load(open(first_pickle, 'rb'))

        fname, ext  = first_pickle.split('.')
        
        # Load the given dataset into memory
        df = Table(fname + '.csv')

        columns = encoder.keys()

        for col in tqdm(columns, ascii=True, desc="Decoding all : "):
            # Pick the encoder
            le = encoder[col]
            df.data[col] = le.inverse_transform(df.data[col])

        output_file =  fname + '_inversed_' + datetime.now().strftime("%d-%B-%Y-%H-%M-%S") + '.csv'
        df.data.to_csv(output_file, index=False)
        print(output_file)
            
    else:
        click.echo('No cognito decoded files found')



def inverse_transform_report():
    """
    Inverse transform pickled encoders and output dataframe to 
    its original form.
    """
    pickles = glob.glob("*.pkl")
    datasets = glob.glob("*.csv")

    if len(pickles) > 0 and len(datasets) > 0:
        
        # pick the first pickle 
        first_pickle = pickles.pop(0)

        # Get the file related the given pickle
        fname = re.sub("\.csv\..*","", first_pickle)

        # Grab the encoder from pickle
        encoder = pickle.load(open(first_pickle, 'rb'))
        columns = encoder.keys()

        # Load the given dataset into memory
        df = Table(fname + '.csv')
        x = PrettyTable()
        x.field_names = ["Feature Name", "% Missing", "Outliers"]
        x.align["Feature Name"] = "l"
       

        for col in tqdm(columns, ascii=True, desc="Decoding all : "):
            le = encoder[col]
            # print(le.inverse_transform(df.data[col].unique))
            # click.echo(col)
            missing = col_missing_percentage(df.data, col)
            x.add_row([col, missing, ''])

        print(x)




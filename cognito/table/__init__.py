'''
Importing all the libraries needed
'''
import pandas as pd
import numpy as np

class Table():
    '''
    Takes a csv file as input and converts to
    dataframe to perform specific operations
    '''
    def __init__(self, filename):
        '''
        Reading the csv file
        '''
        self.data = pd.read_csv(filename)

    def columns(self):
        """
        Get all the column names from the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.columns()
        """
        columns = []
        for column in self.data.columns:
            columns.append(column)
        return columns

    def total_columns(self):
        """
        Get the count of all column in the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_columns()
        """
        columns = []
        for column in self.data.columns:
            columns.append(column)
        return len(columns)

    def total_rows(self):
        """
        Get total count of rows from the current
        dataframe `self.data`.

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_rows()
        """
        return self.data.shape[0]

    def get_categorical(self):
        """
        Gets the categorical columns from the given
        dataframe `self.data`

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.get_categorical()
        """

    def get_numerical(self):
        """
        Gets the numerical columns from the given
        dataframe `self.data`

        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.get_numerical()
        """


    def odd_rows(self):
        """
        Get all odd indexed counted rows from the given
        dataframe `self.data`
        returns: dataframe

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.odd_rows()
        """

    def even_rows(self):
        """
        Get all even indexed counted rows from the given
        dataframe `self.data`

        returns: dataframe
        """

    def apply(self):
        '''
        No description
        '''
        
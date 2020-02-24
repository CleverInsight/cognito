'''
Importing all the libraries needed
'''
import pandas as pd
import numpy as np


class Table:
    """

    Table takes a csv file as input and converts to
    a datframe to perform specific operations.
    """
    def __init__(self, filename):
        self.data = pd.read_csv(filename)


	def data(self):
		"""
		Returns the actual dataframe from taken
		form processing.
		"""
		return self.data


    def columns(self):
        """
        Get all the column names from the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.columns()
        """

        return self.data.columns


    def total_columns(self):
        """
        Get the count of all column in the given
        dataframe `self.data`

        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_columns()
        """

        return len(self.columns())


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
        dataframe = pd.DataFrame()
        for i in self.data:
            if self.data[i].dtypes == 'object':
                dataframe[i] = pd.Series(self.data[i])
        return dataframe

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
        dataframe = pd.DataFrame()
        for i in self.data:
            if np.issubdtype(self.data[i].dtype, np.number):
                dataframe[i] = pd.Series(self.data[i])
        return dataframe


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
        return self.data.iloc[1::2]


    def even_rows(self):
        """
        Get all even indexed counted rows from the given
        dataframe `self.data`

        returns: dataframe
        """


    def apply(self):
        """
        No description
        """


    def summary(self):
        """
        Return the dataframe descriptive statistics

        returns: dataframe summary

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.summary()
        """
        return self.data.describe()

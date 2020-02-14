"""
Data checking module
"""
from __future__ import print_function
import os
import sys
import pandas as pd
import numpy as np
class Check():
    """
    Check class helps us to identify the types of
    variables categorical | Continuous | Discrete
    """
    def __ini__(self):
        pass

    @staticmethod
    def is_working(column="Cognito!"):
        """
        Determines whether the specified command is working.
        :param      column:  The column
        :type       column:  string
        """
        return "Hello, %s! How are you %s?"%(column, column)

    @staticmethod
    def is_categorical(column):
        """
        Determines whether the specified col is categorical.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_categorical(data['Age'])
            >> True
        """

    @staticmethod
    def is_continuous(column):
        """
        Determines whether the specified col is continuous.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_continuous(data['Age'])
            >> False
        """

    @staticmethod
    def is_discrete(column):
        """
        Determines whether the specified column is discrete.

        :param      column:  column name
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_discrete(data['Age'])
            >> True
        """

    @staticmethod
    def is_identifier(column):
        """
        Determines whether the specified column is identifier.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_identifier(data['Age'])
            >> True

        """


    @staticmethod
    def is_missing(column):
        """
        Determines whether the specified column is having missing.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_missing(data['Price'])
            >> False
        """
    @staticmethod
    def is_outlier(column, threshold):
        """
        Returns all the outliers in the column.

        :param      column:   The column
        :type       column:   {pandas.series | list | tuple}
        :return     list:     List of all the ouliers in the column

        Usage:
        =====
           >> Check.is_outlier(data['population'])
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

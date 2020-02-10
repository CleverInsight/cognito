"""
Data checking module
"""
from __future__ import print_function
import os
import sys
import math
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
        return bool(True) if column.nunique() == column.shape[0] else bool(False)

    @staticmethod
    def ignore_identifier(dataframe):
        """
        Drops the table if the column is an identifier.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     DataFrame:Updated DataFrame

        Usage:
        ======
            >> Check.ignore_identifier(data)
            >> Updated Dataframe
        """
        col = list(dataframe)
        for i in col:
            if Check.is_identifier(dataframe[i]):
                dataframe.drop([i], axis=1, inplace=True)
        return dataframe
"""
Data checking module
"""
import os
import sys
import pandas as pd
import numpy as np


class Check(object):

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
        try:
            return True if column.dtypes == 'object' else False

        except AttributeError:

            print("Method only supported pandas.cores.series")
        

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
        pass


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
        pass


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
        pass


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
        pass

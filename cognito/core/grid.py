import pandas as pd
import numpy as np 
import math
import pickle
from collections import Counter
from cognito.logger import logger
from scipy.stats.stats import kendalltau
from scipy.stats import pointbiserialr
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from tqdm import tqdm

class Grid(pd.DataFrame):


    @property
    def _constructor(self):
        return Grid

    @property
    def categorical(self):
        return self.get_categorical().columns.to_list()

    @property
    def continuous(self):
        return self.get_numerical().columns.to_list()
   

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
        for i in self:
            if self[i].dtypes == 'object':
                dataframe[i] = pd.Series(self[i])
        return dataframe


    def get_numerical(self):
        """
        Gets the numerical columns from the given
        dataframe `self`
        returns: dataframe
        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.get_numerical()
        """
        dataframe = pd.DataFrame()
        for i in self:
            if np.issubdtype(self[i].dtype, np.number):
                dataframe[i] = pd.Series(self[i])
        return dataframe



    def is_long_text(self, col, threshold=50):
        """
        Determines if long text.
        
        :param      col:        The col
        :type       col:        { type_description }
        :param      threshold:  The threshold
        :type       threshold:  number
        
        :returns:   True if long text, False otherwise.
        :rtype:     boolean
        """
        return np.all(self[col].str.len() > threshold)


    def total_columns(self):
        """
        Get the count of all column in the given
        dataframe `self`
        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_columns()
        """
        return len(self.columns)
    
    def total_rows(self):
        """
        Get total count of rows from the current
        dataframe `self`.
        returns: dataframe
        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.total_rows()
        """
        return self.shape[0]

    def odd_rows(self):
        """
        Get all odd indexed counted rows from the given
        dataframe `self`
        returns: dataframe
        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.odd_rows()
        """
        return self.loc[:, ::2]
        
    def even_rows(self):
        """
        Get all even indexed counted rows from the given
        dataframe `self`
        returns: dataframe
        """
        return self.loc[:, ::-2]

    def summary(self):
        """
        Return the dataframe descriptive statistics
        returns: dataframe summary
        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.summary()
        """
        return self.describe()
    
    def hot_encoder_categorical(self, column):
        """
        Returns the pandas.series with hashtable in Dict structures
        returns: pandas.series, dict
        Usage:
        ======
            >>> df.hot_encoder_categorical(col_name)
        """
        one_hot = pd.get_dummies(self[column])
        return one_hot  

    def convert_to_bin(self, column):
        """
        Returns the columns with more than 50% threshold to
        newly created bin pandas.series
        returns: pandas.series
        descriptions: list of newly created bin values
        :param      column
        :type       name of the column
        :returns:   list of generated bins
        :rtype:     list

        Weblink: https://www.geeksforgeeks.org/binning-in-data-mining/


        Usage:
        ======
            >>> self.convert_to_bin(col_name)
        """
        length = len(self[column])
        sqr = round(math.sqrt(length))
        maximum = int(max(self[column]))
        minimum = int(min(self[column]))
        bin_size = int(round((maximum - minimum) / sqr))
        quantity = round(maximum/bin_size)
        bins = []
        for low in range(int(minimum - 1), int(minimum + quantity * bin_size + 1), bin_size):
            bins.append((low+1, low + bin_size))
        return bins 

    def correlation(self, mode="pearson"):
        """
        Return the pairwise correlation of the given
        dataframe `self.data` and return dataframe with
        respective dataframe.
        :param      mode:  `Pearson`, `Kendall`, `Spearman`, `Point-Biserial`
        :type       mode:  string
        :returns:   correlation matrix
        :rtype:     dataframe

        Weblink: https://www.geeksforgeeks.org/mathematics-covariance-and-correlation/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.correlation()
        """
        if mode == "pearson":
            pearsoncorr = self.corr(method='pearson')
        elif mode == "kendall":
            pearsoncorr = self.corr(method='kendall')
        elif mode == "spearman":
            pearsoncorr = self.corr(method='spearman')
        return pearsoncorr
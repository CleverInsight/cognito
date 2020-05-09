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

    def covariance(self):
        """
        Return the covariance of the given
        dataframe `self.data` and return dataframe with
        respective dataframe.
        Weblink: https://www.geeksforgeeks.org/mathematics-covariance-and-correlation/
        

        Ref: https://www.theanalysisfactor.com/covariance-matrices/
        returns :  dataframe
        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.covariance()
        """
        result = self.cov()
        return result

    def slice(self, columns):
        """
        Return only the columns sliced
        from `self.data` based on given `columns` parameter
        :param      columns:  list or tuple
        :type       columns:  { list of columns name  }
        returns: dataframe of only given column names.

        weblink:https://www.geeksforgeeks.org/python-slice-function/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.slice(['name', 'age'])
            ---------------
              name  | age
            ---------------
              Sam   | 20
            ---------------
              Jack  | 40
            ---------------
        """
        return self[columns]

    def binning(self, column, bins):
        """
        Return dataframe of select column convert into bins as given
        parameter
        :param      col:   The column
        :type       col:   { column name to be selected }
        :param      bins:  The bins
        :type       bins:  list of  of bins to convert

        weblink: https://www.geeksforgeeks.org/binning-in-data-mining/

        :param      bins:  The bins
        :type       bins:  list of  of bins to convert
        returns: dataframe of given column as bins
        example:
            # Numerical Binning Example

                Value      Bin
                0-30   ->  (0-30)
                31-70  ->  (31-70)
                71-100 ->  (71-100)


            # Categorical Binning Example
                Value      Bin
                Spain  ->  Europe
                Italy  ->  Europe
                Chile  ->  South America
                Brazil ->  South America
        Usage:
            >>> df = Table('filename.csv')
            >>> df.binning('age', bins=[], labels=['low', 'med', 'high'])
            ------------------
            |  age  | age_bin
            ------------------
            |  14   | low
            ------------------
            |  90   | high
            ------------------
            |  14   | low
            ------------------
            |  40   | middle
            ------------------
            |  14   | low
            ------------------
        """
        binned_weight = []
        data = pd.DataFrame(columns=['Value', 'Bin'])
        for val in self[column]:
            for i in range(0, len(bins)):
                if bins[i][0] <= val < bins[i][1]:
                    data = data.append({'Value':val, 'Bin':bins[i]}, ignore_index=True)
                    binned_weight.append(i)
        freq = Counter(binned_weight)
        return (data, freq)


    def fix_outlier_with_std_deviation(self, column):
        """
        Take the column from `self.data` and check for outlier
        fix the outlier using mode : std deviation
        Ref: https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
        :param      column:  The column
        :type       column:  { column name as string }
        :param      mode:  mode like std deviation
        :type       column:  { string }
        returns: dataframe without outlier

        Weblink: https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html

        Usage:
        ======
            >>> df = Table('filename.csv')

            >>> df.fix_outlier_with_std_deviation('age', 3)
        """
        outliers = []
        mean = np.mean(self[column])
        std_dev = np.std(self[column])
        for value in self[column]:
            z_score = (value - mean) / std_dev
            if np.abs(z_score) > 3:
                outliers.append(value)
        for i, _ in enumerate(self[column]):
            if i in outliers:
                i.replace(std_dev, inplace=True)
        return self[column]

    def ignore_cardinal(self):
        """
        Take the dataframe `self.data` and remove all cardinality columns
        and return the dataframe
        returns: dataframe without cardinality columns

        Weblink:https://www.geeksforgeeks.org/python-named-entity-recognition-ner-using-spacy/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.ignore_cardinal()
        """
        data = self.copy()
        for i in data:
            if len(data[i]) == data[i].nunique(dropna=True):
                data.drop(i, axis=1, inplace=True)
        return data


    def fix_missing(self, column):
        """
        Take the column from `self.data` and fix the type of columns
        and clean the missing values based on categorical or numerical
        :param      column:  The column
        :type       column:  { column name }
        returns: dataframe | pandas.core.series

        Weblink: https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.fix_missing('age')
        """
        self.ignore_cardinal()
        continuous = self.get_numerical().columns.tolist()
        categorical = self.get_categorical().columns.tolist()
        if column in continuous:
            self[column].fillna(self[column].mean(), inplace=True)
        elif column in categorical:
            self[column].fillna(self[column].mode()[0], inplace=True)
        return self[column]

    def cardinal_columns(self):

        all_columns = self.columns
        excluded_cardinal = self.ignore_cardinal().columns

        set_difference = set(all_columns) - set(excluded_cardinal)
        return list(set_difference)

    def drop_cardinality(self):
        """
        Create cardinality columns
        
        :returns:   { description_of_the_return_value }
        :rtype:     { return_type_description }
        """
        cardinal_cols = self.cardinal_columns()
        self = self.drop(cardinal_cols, axis=1)
    

    
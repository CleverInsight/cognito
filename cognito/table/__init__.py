'''
Importing all the libraries needed
'''
import pandas as pd
import numpy as np
from scipy.stats.stats import kendalltau
from scipy.stats import pointbiserialr


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
        # TODO:

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


    def hot_encoder_categorical(self, column):
        """
        Returns the pandas.series with hashtable in Dict structures

        returns: pandas.series, dict

        Usage:
        ======
            >>> self.hot_encoder_categorical(col_name)
        """
        pass


    def convert_to_bin(self, column):
        """
        Returns the columns with more than 50% threshold to 
        newly created bin pandas.series

        returns: pandas.series 
        descriptions: list of newly created bin values

        Usage:
        ======
            >>> self.convert_to_bin(col_name)
        """
        pass

    def correlation(self, mode="pearson"):
        """
        # TODO:

        Return the pairwise correlation of the given 
        dataframe `self.data` and return dataframe with
        respective dataframe.

        Ref: http://www.real-statistics.com/statistics-tables/pearsons-correlation-table/

        
        :param      mode:  `Pearson`, `Kendall`, `Spearman`, `Point-Biserial`
        :type       mode:  string
        
        :returns:   correlation matrix
        :rtype:     dataframe

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.correlation()
        
        """
        if(mode == "pearson"):
            pearsoncorr = self.data.corr(method='pearson')
            return pearsoncorr
        elif (mode == "kendall"):
            pearsoncorr = self.data.corr(method='kendall')
            return pearsoncorr
        elif (mode == "spearman"):
            pearsoncorr = self.data.corr(method='spearman')
            return pearsoncorr
        

        pass

    def covariance(self):
        """
        # TODO:

        Return the covariance of the given 
        dataframe `self.data` and return dataframe with
        respective dataframe.

        Ref: https://www.theanalysisfactor.com/covariance-matrices/

        returns :  dataframe 

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.correlation(
        """

        pass



    def slice(self, columns):
        """
        # TODO:

        Return only the columns sliced 
        from `self.data` based on given `columns` parameter

        
        :param      columns:  list or tuple
        :type       columns:  { list of column name  }

        returns: dataframe of only given column names.

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
        # TODO:

        pass



    def binning(self, col, bins, labels):
        """
        Return dataframe of select column convert into bins as given
        parameter
        
        :param      col:   The col
        :type       col:   { column name to be selected }
        :param      bins:  The bins
        :type       bins:  list of  of bins to convert
        :param      bins:  The bins
        :type       bins:  list of  of bins to convert

    
        returns: dataframe of given column as bins

        example:
            # Numerical Binning Example
                Value      Bin       
                0-30   ->  Low       
                31-70  ->  Mid       
                71-100 ->  High

            # Categorical Binning Example
                Value      Bin       
                Spain  ->  Europe      
                Italy  ->  Europe       
                Chile  ->  South America
                Brazil ->  South America


        Usage:
        ======



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
        # TODO:

        pass


    def fix_outlier(self, column, mode):
        """
        Take the column from `self.data` and check for outlier 
        fix the outlier using mode : std deviation, percentile, drop and cap

        Ref: https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
        
        :param      column:  The column 
        :type       column:  { column name as string }
        
        :param      mode:  mode like std deviation, percentile, drop and cap
        :type       column:  { string}

        returns: dataframe without outlier

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.fix_outlier('age', 'drop')

        """

        # TODO:

        pass



    def fix_missing(self, column):
        """
        Take the column from `self.data` and fix the type of columns
        and clean the missing values based on categorical or numerical
        
        :param      column:  The column
        :type       column:  { column name }

        returns: dataframe | pandas.core.series

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.fix_missing('age')

        """

        # TODO:

        pass


    def imputer(self, column, value):
        """
        Take the columns from `self.data` and fill the missing NA
        values with given value parameter based on the type of column
        
        :param      column:  The column
        :type       column:  { column name }

        :param      value:  The value by which NA will be replaced
        :type       value:  { string, number, boolean}
        returns: dataframe | pandas.core.series

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.imputer('age', 10)
        """

        # TODO:

        pass


    def ignore_cardinal(self):
        """
        Take the dataframe `self.data` and remove all cardinality columns
        and return the dataframe
        
        returns: dataframe without cardinality columns

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.ignore_cardinal()

        """

        # TODO:

        pass


    def encode_column(self, column):
        """
        Encodes a column using the numerical values and 
        return the dictionary for mapping.
        
        :param      column:  The column
        :type       column:  { column name }

        returns: dataframe, mapper dictionary
        
        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.encode_column('Country')
            >>> (dataframe, {'0': 'US', '1': 'India', '2': 'Europe'})

        """

        # TODO:
        
        pass




    def scale(self):
        
        # TODO

        # IMPORTANT function to be discussed

        pass




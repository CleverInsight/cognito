#pylint: disable = E0202
#pylint: disable = R0904
#pylint: disable = C0200
#pylint: disable = E0602
#pylint: disable = C0103
'''
Importing all the libraries needed
'''
import pickle
import math
from collections import Counter
import pandas as pd
import numpy as np
from scipy.stats.stats import kendalltau
from scipy.stats import pointbiserialr
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from tqdm import tqdm


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
        return self.data.iloc[:-2:2]


    #def apply(self):


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
            >>> df.hot_encoder_categorical(col_name)
        """
        one_hot = pd.get_dummies(self.data[column])
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
<<<<<<< HEAD

        Weblink: https://www.geeksforgeeks.org/binning-in-data-mining/


=======
>>>>>>> a0dc96e323316a85c3b913517ea5819103ce1ed5
        Usage:
        ======
            >>> self.convert_to_bin(col_name)
        """
        length = len(self.data[column])
        sqr = round(math.sqrt(length))
        maximum = int(max(self.data[column]))
        minimum = int(min(self.data[column]))
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
            pearsoncorr = self.data.corr(method='pearson')
        elif mode == "kendall":
            pearsoncorr = self.data.corr(method='kendall')
        elif mode == "spearman":
            pearsoncorr = self.data.corr(method='spearman')
        return pearsoncorr


    def covariance(self):
        """
        Return the covariance of the given
        dataframe `self.data` and return dataframe with
        respective dataframe.
<<<<<<< HEAD
        Weblink: https://www.geeksforgeeks.org/mathematics-covariance-and-correlation/
        
=======
        Ref: https://www.theanalysisfactor.com/covariance-matrices/
>>>>>>> a0dc96e323316a85c3b913517ea5819103ce1ed5
        returns :  dataframe
        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.covariance()
        """
        result = self.data.cov()
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
        return self.data[columns]


    def binning(self, column, bins):
        """
        Return dataframe of select column convert into bins as given
        parameter
        :param      col:   The column
        :type       col:   { column name to be selected }
        :param      bins:  The bins
        :type       bins:  list of  of bins to convert
<<<<<<< HEAD

        weblink: https://www.geeksforgeeks.org/binning-in-data-mining/

=======
        :param      bins:  The bins
        :type       bins:  list of  of bins to convert
>>>>>>> a0dc96e323316a85c3b913517ea5819103ce1ed5
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
        for val in self.data[column]:
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
        mean = np.mean(self.data[column])
        std_dev = np.std(self.data[column])
        for value in self.data[column]:
            z_score = (value - mean) / std_dev
            if np.abs(z_score) > 3:
                outliers.append(value)
        for i, _ in enumerate(self.data[column]):
            if i in outliers:
                i.replace(std_dev, inplace=True)
        return self.data[column]


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
            self.data[column].fillna(self.data[column].mean(), inplace=True)
        elif column in categorical:
            self.data[column].fillna(self.data[column].mode()[0], inplace=True)
        return self.data[column]


    def imputer(self, column, value):
        """
        Take the columns from `self.data` and fill the missing NA
        values with given value parameter based on the type of column
        :param      column:  The column
        :type       column:  { column name }
        :param      value:  The value by which NA will be replaced
        :type       value:  { string, number, boolean }
        returns: dataframe | pandas.core.series

        Weblink: https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.imputer('age', 10)
        """
        self.data[column].fillna(value, inplace=True)
        return self.data[column]


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
        data = self.data.copy()
        for i in data:
            if len(data[i]) == data[i].nunique(dropna=True):
                data.drop(i, axis=1, inplace=True)
        return data


    def encode_column(self, column):
        """
        Encodes a column using the numerical values and
        return the dictionary for mapping.
        :param      column:  The column
        :type       column:  { column name }
        returns: dataframe, mapper dictionary

        Weblink: https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.encode_column('Country')
            >>> (dataframe, {'0': 'US', '1': 'India', '2': 'Europe'})
        """
        encode = LabelEncoder()
        data = encode.fit_transform(self.data[column])
        return data, encode


    def list_cardinal(self):
        """
        Return the list of all cardinality columns from the given
        `self.data`
        :returns:   { list of all cardinality values }
        :rtype:     { List }
        """
        return [col for col in self.data if len(self.data[col]) == self.data[col].nunique()]


    def generate(self):
        """
        No docstring for the time being
        """
        cardinal_col = self.list_cardinal()
        categorical_col = list_diff(self.get_categorical().columns, cardinal_col)
        numerical_col = list_diff(self.get_numerical().columns, cardinal_col)

        # Fix categorical and numerical columns
        for col in tqdm(categorical_col + numerical_col, ascii=True, desc="Imputing missing : "):
            self.fix_missing(col)

        data = self.data.drop(cardinal_col, axis=1)

        # Encode categorical variables
        encoders = {}

        for col in tqdm(categorical_col, ascii=True, desc="Encoding : "):
            x, y = self.encode_column(col)
            data[col] = x
            encoders[col] = y

        return data, encoders


    def scale(self, columns, mode='minmax'):
        """
        Take a dataframe self.data and list of columns, scales the feature with distribution value
        between 0 and 1
        :param      column:  columns
        :type       column:  [list of colums to be scaled]
        :param      column:  mode
        :type       column:  mode for scaling  MinMax/std_dist
        returns: dataframe of columns after scaling

        Weblink: https://www.geeksforgeeks.org/scales-of-measurement/

        Usage:
        ======
            >>> df = Table('filename.csv')
            >>> df.scale(columns, mode)
            >>> dataframe
        """
        original_data = self.slice(columns)
        if mode == 'minmax':
            scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
            transformed_data = scaler.fit_transform(original_data)
        elif mode == 'std_dist':
            scaler = preprocessing.StandardScaler()
            transformed_data = scaler.fit_transform(original_data)
        return transformed_data


    def categorical_columns(self):
        """
        Get only the categorical columns
        
        :returns:   { description_of_the_return_value }
        :rtype:     { return_type_description }
        """
        return self.get_categorical().columns

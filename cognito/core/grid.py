import pandas as pd
import numpy as np 



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
        dataframe `self.data`
        returns: dataframe
        Usage:
        ======
            >>> data = Table('filename.csv')
            >>> data.odd_rows()
        """
        return self.iloc[1::2]

    
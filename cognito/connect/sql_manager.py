import yaml
import pandas as pd
import mysql.connector as sql
from cognito.logger import logger
from cognito.table import Table

__AUTHOR__ = 'Bastin Robins J'


class SQL:
    """
    Class that takes the SQL connection parameters and establish the
    connection successfully and convert to cognito dataframes. 
    """
    def __init__(self, filepath):
        # Read the yaml configuration
        with open(filepath) as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)
            try:
                self.connect = sql.connect(**self.config['credentials'])
                logger.success("Database connection established successfully")
            except Exception as e:
                logger.warning("Invalid credentials")

            self.data = Table(pd.read_sql(self.config['query'], con=self.connect, index_col=None))
            self.categorical = self.data.categorical_columns()
            self.numerical = self.data.numerical_columns()
            self.identifier = self.data.cardinal_columns()

            

    def info(self):
        """
        Get the information about the configuration passed
        
        :returns:   { dict }
        :rtype:     { configuration passed into Parent class }
        """
        return self.config


    def tables(self):
        """
        Get database tables list
        
        :returns:   { List of all table names }
        :rtype:     { dataframe }
        """
        query = "SELECT table_name FROM information_schema.tables \
        WHERE table_schema = '{}'".format(self.config['credentials']['database'])
        df = pd.read_sql(query, con=self.connect)
        return df


    def dataframe(self, ignore_cols=[]):
        
        if len(ignore_cols) > 0:
            return self.data

        return self.data





    def save(self, filename):
        self.data.save(filename)

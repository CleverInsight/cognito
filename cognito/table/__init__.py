import pandas as pd
import numpy as np


class Table:

	def __init__(self, filename):
		self.data = pd.read_csv(filename)


	def data(self):
		"""
		Returns the actual dataframe from taken
		form processing
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
		pass

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
		df=pd.DataFrame()
		for i in self.data:
			if self.data[i].dtypes=='object':
				df[i]=pd.Series(self.data[i])
		return df
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
		df=pd.DataFrame()
		for i in self.data:
			if np.issubdtype(self.data[i].dtype, np.number):
				df[i]=pd.Series(self.data[i])
		return df


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
		pass

	def even_rows(self):
		"""
		Get all even indexed counted rows from the given
		dataframe `self.data`

		returns: dataframe
		"""
		pass

	def apply(self):
		pass
data=Table('C:/Users/HP/Desktop/cognito/tests/data/cereal.csv')
data.get_categorical().to_csv('C:/Users/HP/Desktop/cognito/tests/data/cereal_get_categorical.csv')
#data.get_categorical().to_csv('C:/Users/HP/Desktop/cognito/tests/data/Freedman_get_categorical.csv')
#print(data.get_numerical())
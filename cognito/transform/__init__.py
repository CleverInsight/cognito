import os
import sys
import pandas as pd

class Transform:

	def __init__(self):
		pass

	def split_date(x):
		"""
		Split the given string `x` into `day,month,year`
		
		:parameter_description x:	date
		:type_description x:	string
		:return		return Dict
		
		Usage:
		======
			>> T = Transform()
			>> T.__split_date('2020-10-18')
			>> {'day': 18, 'month': 10, 'year': 2020 }

		"""
		import datetime
		li = x.split('-')
		date = ("-").join(li)
		d = datetime.datetime.strptime(date, "%d %b %Y")
		list1 = [d.day,d.month,d.year]
		list2 = ['day','month','year']
		res = {list2[i]: list1[i] for i in range(len(list2))} 
		return res

	@staticmethod
	def split_dates(x):
		"""
		Splits dates given as `pandas.core.series` into multple
		columns consist of `day, month, year` using the above
		`__split_date` private method.
		
		:param      x:    { parameter_description }
		:type       x:    { type_description }
		return 		pandas.core.series

		Usage:
		======
			>> Transform.split_dates([2020-10-02, 2019-10-01, 2020-11-11])
			>> day, month, year
			    02     10   2020
			    01     10   2019
			    11     11   2020

		"""
		date_dict = {'day': [2, 1, 11], 'month': [10, 10, 11], 'year': [2020, 2019, 2020]}
		return pd.DataFrame.from_dict(date_dict)

	@staticmethod
	def numerical(column):
		"""
		Given a `pandas.core.series` consist of categorical data
		encode it into numerical mapping.
		
		:param      column:  list of categorical values
		:type       column:  pandas.core.series
		:return     list of dictionary consisting of key: value

		Usage:
		======
			>> T = Transform()
			>> T.numerical(['cat', 'rat', 'mice', 'mice', 'rat'])
			>> [
				'cat':  0,
				'rat':  1,
				'mice': 3
				]
		"""
		encoded = column.astype('category').cat.codes
		encoded_col = list(encoded)
		describe_encoding = pd.Series(encoded_col, index=column).to_dict()
		return describe_encoding

import os
import sys

class Transform:

	def __init__(self):
		pass

	@staticmethod
	def split_date(x):
		"""
		Split the given string `x` into `day,month,year`
		
		:param      x:    date
		:type       x:    string
		:return     return Dict
		
		Usage:
		======
			>> Transform.split_date('2020-10-18')
			>> {'day': 18, 'month': 10, 'year': 2020 }

		"""
		pass


	def split_dates(x):
		"""
		Splits dates given as `pandas.core.series` into multple
		columns consist of `day, month, year`
		
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
		pass
